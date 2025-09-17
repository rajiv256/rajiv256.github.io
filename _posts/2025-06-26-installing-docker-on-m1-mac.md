---
title: "installing docker on M1 Mac"
permalink: "/blog/installing-docker-on-m1-mac"
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

# Installing docker on M1 Mac

First install `docker` using brew with `cask` option. Note that in newer
macs `brew install` doesn't work as it is a system level package. Or so
StackOverflow says.

> `brew install --cask docker`

Check the status

> `docker ps`

I am working on starting a Neo4j instance. So first

> `pip install neo4j`

Then run the docker instance for neo4j

> `docker run -h "neo4j/latest" -p7474:7474 -p7687:7687 -d -e NEO4J_AUTH neo4j/secretpassword neo4j/latest`

`-d` means to detach, so the instance might be running in the
background. You can check that using

> `ps -ef | grep docker`

[Edit](https://github.com/rajiv256/rajiv256.github.io/edit/main/_posts/2025-06-26-installing-docker-on-m1-mac.md)
