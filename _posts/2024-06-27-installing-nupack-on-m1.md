---
title: "Installing NUPACK on M1 Mac"
permalink: "/blog/installing-nupack-on-m1-mac"
categories: "DNA Computing"
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
tags: dna-computing
---

# Installing NUPACK on M1 Mac \>.\<

Let’s be honest. The M1 Mac was designed to make the already hard life
of graduate students who code much harder. I was trying to install
NUPACK and it failed me in more ways than my eight standard economics
quiz. I am not really a rule follower so I also don’t follow the
official documentation word-by-word which could also be a ‘small’ and
‘insignificant’ reason for my troubles. Either way, closely following
the <a href="https://docs.nupack.org/start/#maclinux-installation">
official documentation</a> could get you where you want to.

I am gonna repeaat the instructions here so that you’d be assured that
atleast someone got it working on an M1. The documentation linked above
first asks you to download the version of NUPACK from the official page
that is marked as “M1”. Hand to God, I didn’t find a single distribution
that was labeled “M1”. So, I did eenie-meenie-monie with the
distributions and picked…just kidding. Like any respectable computer
scientist would, I picked the latest version.

*The first thing we do, let’s kill all the lawyers Shakespeare
([2001](#ref-shakespeare2001henry)).* No don’t. The first thing we do is
download Python 3.8 or higher. Keep in mind two things. (1) The version
must be 3.8+. (2) Make sure the python used is native. That means no
virtual environment business. Use the python that’s installed in your
PC. Here’s my executable:

`$ which python3`

`/opt/homebrew/bin/python3`

`$ python3 --version`

`Python 3.10.8`

I then proceeded to read Cloud Atlas. Oops, wrong timeline. I then
proceeded to unzip the downloaded NUPACK folder.

`$ unzip nupack-VERSION.zip`

Now simply install the nupack package from the downloaded file as
follows:

`$ python3 -m pip install -U nupack -f nupack-VERSION/package`

And that’s it. Try to execute `import nupack` and you should succeed. If
you don’t succeed, well, it’s your own fault for buying your stupid M1.

<div id="refs" class="references csl-bib-body">

<div id="ref-shakespeare2001henry" class="csl-entry">

Shakespeare, W. (2001) *Henry VI.: Part three*. Oxford University Press,
USA.

</div>

</div>
