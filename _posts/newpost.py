"""
Filename: newpost.py

Author: rajiv256

Created on: 28-06-2024

Description:
"""

# begin imports
import os
import sys
import random
import seaborn as sns
import argparse
import logging
import pickle as pkl

from tqdm import tqdm
import matplotlib.pyplot as plt
# end imports

# begin code

s = f'''
---
title: "{title}"
permalink: "/blog/{'-'.join(title.lower().split())}"
categories: ""
output:
  md_document:
    variant: kramdown
    preserve_yaml: TRUE
    pandoc_args: 
      - "--wrap=preserve"
knit: (function(inputFile, encoding) {
  rmarkdown::render(inputFile, encoding = encoding, output_dir = "../_posts") })

layout: single
bibliography: refs.bib
link-citations: true
defaults:
- scope:
    path: ''
    type: posts
  values:
    author_profile: false
    read_time: true
    comments: true
    share: true
    related: true
    breadcrumbs: false
tags: 
---'''
def get_args():
    parser = argparse.ArgumentParser("Arguments.")


    args = parser.parse_args()
    return args





if __name__=="__main__":
    opt = get_args()

