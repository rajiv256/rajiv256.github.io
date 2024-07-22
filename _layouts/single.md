---
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
defaults:
- scope:
    path: ''
    type: posts
---

{{ content }}
