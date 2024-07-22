---
title: "Nucleic Acid Amplification"
permalink: "/blog/nucleic-acid-amplification"
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

# Nucleic acid amplification

Nucleic acid amplification (NAA) plays an important rule in pathological
testing, especially in the diagnosis of infectious diseases and genetic
disorders. Rapid amplification requires the use of enzymes. And so they
do.

Notomi *et al.* ([2000](#ref-Notomi2000)) is the first popular model for
performing NAA and introduced a method known as Loop-mediated Isothermal
Amplification, that uses an arguably incongruous acronym known as LAMP.
It is called so because the amplification starts with a primer pairing
to a loop in the stem-loop structure. So, it is mediated by the loop.

The method uses DNA Polymerase. The ‘target’ strand contains *6
recognition sites*. It contains *4 different primers* — 2 inner primers
and 2 outer primers.

The amplification process contains *forward* sites and *backward* sites
aka ‘sense’ and ‘antisense’ strands. So the DNAP action runs in both
directions. An interesting point is that the primers are designed so
that the action of inner primers is faster than that of the outer
primers. The target contains the forward sites on the $3'$ end and the
backward sites in the $5'$ end.

The amplification process consists of the following steps:

1.  **Prepare the stem-loop** — Starts from a single-stranded ‘target’
    strand and through a set of DNAP synthesis through inner and outer
    primers, a double loop structure is formed in the form of dumbbells
    at both the helix ends. This quickly transforms into a stem-loop
    structure following a DNAP action.
2.  **Amplification** —

<div id="refs" class="references csl-bib-body">

<div id="ref-Notomi2000" class="csl-entry">

Notomi, T. *et al.* (2000) ‘Loop-mediated isothermal amplification of
DNA’, *Nucleic Acids Res.*, 28(E63).

</div>

</div>
