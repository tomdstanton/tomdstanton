from datetime import datetime
import os
import slugify  # pip install python-slugify

def create_eleventy_post(title, description, tags=[]):
    # Set target directory (adjust path based on your folder structure)
    posts_dir = "src/posts" 
    os.makedirs(posts_dir, exist_ok=True)
    
    # Format metadata
    date_str = datetime.now().strftime("%Y-%m-%d")
    file_slug = slugify.slugify(title)
    filename = f"{date_str}-{file_slug}.md"
    filepath = os.path.join(posts_dir, filename)
    
    # Structure Eleventy front-matter
    front_matter = (
        "---\n"
        f'title: "{title}"\n'
        f'description: "{description}"\n'
        f"date: {date_str}\n"
        f"tags: {tags}\n"
        "layout: post\n"
        "---\n\n"
        "Start writing your content here..."
    )
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(front_matter)
    
    print(f"Success! Created new draft at: {filepath}")

# Example usage:
if __name__ == "__main__":
    create_eleventy_post(
        title="My Automated Python Post",
        description="This post was created completely using a Python automation script.",
        tags=["python", "automation"]
    )

