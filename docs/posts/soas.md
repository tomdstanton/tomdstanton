---
draft: true
date: 2026-06-28T23:08:01.653Z
title: You like 'Huey Lewis and the News'?
description: Data-oriented-design in bioinformatics
author: "Tom Stanton"
comments: true
---

It's hip to be square - 

![](https://miro.medium.com/v2/resize:fit:1000/format:webp/1*Qa7su6VMnUUu_fCrKg4vtA.gif)

## Operations on squares, not objects.

Numpy is [**fantastic**](https://chelseatroy.com/2018/11/07/code-mechanic-numpy-vectorization/)
for vectorisation - and consequently so is Pandas. Also, so are some of my favourite `tidyverse`
functions: `mutate()`, `if_else()` and `across()`.

This means you have to think less about your data when it is in a tabular format, but more about how to represent your data abstractions inside a tabular format.
You may think this is easy, but let's use the following example:

```python
from dataclasses import dataclass
from typing import Literal

@dataclass
class Gene:
	name: str
	start: int
	end: int
	strand: Literal[-1, 0, 1]
```

We have defined a simple `Gene` model, representing a gene on a chromosome with a name, coordinatedes, and orientation.
But say I want to 