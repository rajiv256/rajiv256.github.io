"""
Filename: newpost.py

Author: rajiv256

Created on: 28-06-2024

Description:
  python3 newpost.py --title "xyz"
"""

# begin imports
import os
import sys
import random
import argparse
import logging
import pickle as pkl
from datetime import datetime

import matplotlib.pyplot as plt
# end imports

# begin code

def newpost(title="This is Title"):

  s = f'''---
title: "{title}"
permalink: "/blog/{'-'.join(title.lower().split())}"
categories: ""
layout: postpage
bibliography: refs.bib
link-citations: true
scholar:
  locale: en
output:
  md_document:
    variant: gfm
    preserve_yaml: true
    dev: "png"
    df_print: default
csl: citations.csl
---
'''
  dateformat = datetime.today().strftime("%Y-%m-%d")
  filename = dateformat + "-" + "-".join(title.lower().split())+".md"

  with open(filename, "w+") as fout:

    fout.write(s + '\n')
    fout.write("# " + title + "\n")
    fout.write(f"[Edit](https://github.com/rajiv256/rajiv256.github.io/edit/main/_posts/{filename})")


def get_args():
    parser = argparse.ArgumentParser("Arguments.")

    parser.add_argument("--title", type=str, required=True)
    args = parser.parse_args()
    return args





if __name__=="__main__":
    opt = get_args()

    newpost(opt.title)

