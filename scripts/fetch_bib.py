# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

import json
import urllib.request
import os
from pathlib import Path
from sys import argv

def format_vancouver_authors(authorships):
    """Format a list of OpenAlex authorships into Vancouver style."""
    formatted = []
    for authorship in authorships:
        display_name = authorship.get('author', {}).get('display_name', '')
        if not display_name:
            continue
        parts = display_name.split()
        if len(parts) > 1:
            last = parts[-1]
            firsts = parts[:-1]
            initials = "".join([f[0].upper() for f in firsts if f])
            formatted.append(f"{last} {initials}")
        else:
            formatted.append(display_name)
    
    if len(formatted) > 6:
        return ", ".join(formatted[:6]) + ", et al"
    return ", ".join(formatted)

def format_vancouver(work):
    """Format an OpenAlex work into Vancouver style citation."""
    authors = format_vancouver_authors(work.get('authorships', []))
    title = work.get('title', '')
    if title:
        title = title.replace('\n', ' ')
    else:
        title = ''
        
    journal = ''
    primary_location = work.get('primary_location') or {}
    source = primary_location.get('source') or {}
    if source.get('display_name'):
        journal = source.get('display_name')
        
    year = work.get('publication_year', '')
    
    biblio = work.get('biblio') or {}
    volume = biblio.get('volume', '')
    issue = biblio.get('issue', '')
    first_page = biblio.get('first_page', '')
    last_page = biblio.get('last_page', '')
    
    pages = ''
    if first_page:
        pages = str(first_page)
        if last_page and last_page != first_page:
            pages += f"-{last_page}"
            
    doi_url = work.get('doi', '')
    
    citation = f"{authors}. {title}. "
    if journal:
        citation += f"*{journal}*. "
    if year:
        citation += f"{year};"
    if volume:
        citation += f"{volume}"
    if issue:
        citation += f"({issue})"
    if pages:
        citation += f":{pages}"
    if doi_url:
        citation += f". [DOI]({doi_url})"
    else:
        citation += "."
        
    return citation

def main():
    url = "https://api.openalex.org/works?filter=author.id:https://openalex.org/A5025916428,type:article|proceedings-article&per-page=100"
    
    if api_key := os.environ.get("OPENALEX_API_KEY"):
        url += f"&api_key={api_key}"
        
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Zensical-Bib-Fetcher/1.0')
    
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Failed to fetch data from OpenAlex: {e}")
        return

    works = data.get("results", [])

    with Path('docs/bib.md').open("w", encoding="utf-8") as fh:
        fh.write("""---
title: Bibliography
author: Tom Stanton
comments: true
tags: [markdown, documentation, web]
icon: lucide/book-open-text
---

Below is a pull of my current publications from OpenAlex in no particular order.

""")

        for n, work in enumerate(works, start=1):
            if not work.get("title"):
                continue
            
            vancouver_citation = format_vancouver(work)
            fh.write(f"{n}. {vancouver_citation}\n\n")

if __name__ == "__main__":
    main()
