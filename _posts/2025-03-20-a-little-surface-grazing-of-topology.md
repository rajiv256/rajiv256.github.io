---
title: "Topology of surfaces, or is saying that redundant?"
permalink: /blog/a-little-surface-grazing-of-topology/
date: 2025-03-21
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

All roads lead to Rome. But I must say, this journey into topology was
embarked from a pavement. Without wasting much time on my kitschy yet
romantic exposition of how we got there, let’s dive in into Topology. I
am mostly following the Introduction to Topology by Kinsey. Why? ’Cause
my advisor told so, that’s why. I am listening to this slowed down
bollywood with added rain effects (idk it’s soothing) while I do so:
[link](https://www.youtube.com/watch?v=IEEFSlkKR_U).

The textbook starts with a quintessential example of turning a doughnut
into a coffee cup. Wish I could also pass on all those extra calories.
Topology is essentially the study of special properties of surface that
are invariant to squishing, squeezing, bending, and stretching. But
don’t break it, god forbid!

> Two objects are topologically identical if there is a continuous
> deformation from one to another. In that way, it could be considered
> ’’rubber-sheet geometry” apparently. This topological equivalence is
> also referred to as being *homeomorphic*.

That being said, we start with the first chapter, the simpler of all,
the *Point-set topology*.

## Chapter 1: Point-set topology

The study of the most general possible object: a set of points. For now,
we will constrain to the real *n-space*, $\mathbb R^n$.

A *disc* is typically used to discuss a neighborhood, but this is a
misnomer. It essentially represents a $n-$dimensional sphere that is the
neighborhood defined in terms of the Euclidean distance.

The *interior*, *exterior*, and *boundary* or *limit* points are
determined depending on the nature of their neighborhood.

The *closure* $Cl(A)$ is the set of all limit points of $A$ and is a
closed set.

A function $f: X\to Y$ is a *homeomorphism* iff it is continuous,
invertible, and its inverse function $f^{-1}$ is also continuous. The
spaces $X$ and $Y$ are topologically equivalent.

Topological equivalence is an equivalence relation, meaning it’s
symmetric, reflexive, and transitive.

A set of points is *compact* if every infinite sequence of points in $A$
has a limit point in $A$.

- The real line is not compact since the sequence
  $\{1, 2, 3, 4, \cdots\}$ consists of points in $\mathbb R$ but has no
  limit point in $\mathbb R$. Furthermore, $(0, 1)$ is also not compact.

Intuitively and by *Heine-Borel* theorem, a compact set is both closed
and bounded.

Accordingly, a cube is compact.

Have gone through multiple chapters in the book. Mostly these chapters
were on point-set topology and connectedness, product spaces, and
quotient spaces. These are not my main focus but I acknowledge that some
kind of foundation on them is useful. With that said, I switch into the
chapter on *Surfaces*.

## Chapter 2: Surfaces

A topological complex could be constructed by glueing the similarly
labeled edges together while being cognizant of the edge directions. For
example, for glueing, both the edges should be in the same direction.

A cylinder can be constructed by glueing one set of opposite edges
together.

<figure>
<img src="images/clipboard-3726792012.png" alt="Figure 1" />
<figcaption aria-hidden="true">Figure 1</figcaption>
</figure>

A torus can be constructed by gluing both the opposite edges of a
rectangle.

<figure>
<img src="images/clipboard-2784638289.png" alt="Figure 2" />
<figcaption aria-hidden="true">Figure 2</figcaption>
</figure>

A disk with a zipper, i.e., both the semicircles having the same
direction, is topologically equivalent to a sphere’s surface.

There are ofcourse, many different planar diagrams for any surface.

On the other hand, to represent a mobius strip, the opposite edges to be
glued in the rectangle should be pointing in the opposite directions so
that one of the edges have to be twisted so as to be glued to the other.
The mobius strip however, has only one side, in contrast to the
cylinder.

<figure>
<img src="images/clipboard-1765628320.png" alt="Figure 3" />
<figcaption aria-hidden="true">Figure 3</figcaption>
</figure>

A *manifold* is a topological space such that every point has a
neighborhood topologically equivalent to a $n-$ dimensional open disk
with center $\mathbf{x}$ and radius $r$. A two-dimensional manifold is
often called a surface.

This implies manifolds are Hausdorff spaces.

In classifying the surfaces, the ability to “enclose a cavity” will turn
out to be a distinguishing feature.

Removing two discs from two tori and gluing them together to obtain a
2-handled torus. Notice that the planar polygon for an orientable
surface is a $4g$ sided polygon, given that $g$ is the genus.

<figure>
<img src="images/clipboard-1892683657.png" alt="Figure 4" />
<figcaption aria-hidden="true">Figure 4</figcaption>
</figure>

While it might seem odd that for a homeomorphism, cutting is not
allowed, any cut can be repaired by gluing things back just the way they
were.

### Classification of surfaces

Every compact connected surface is homeomorphic to a sphere, a connected
sum of $n$ tori, or a connected sum of $n$ projective planes. The steps
involved in classifying the surface are as follows.

**Step 1: Build a planar model of the surface**

Since $S$ is a compact surface, there is a simplical complex on it with
finitely many triangles. Since $S$ is connected, its triangles can be
rearranged so that each triangle is glued to an earlier one. Then,
assemble them in the chosen order to form a polygon representing a
planar diagram of the surface.

A surface is connected iff a triangulation can be re-arranged in the
order $T_1, T_2, ..., T_n$ such that each $T_i$ has atleast one edge
common with $T_{i-1}$.

**Step 2: A shortcut**

A string of edges that occur twice in exactly the same order, taking
into account the directions of the edges, we can relabel to consider the
string as a single edge.

<figure>
<img src="images/clipboard-588233091.png" alt="Figure 5" />
<figcaption aria-hidden="true">Figure 5</figcaption>
</figure>

Note that the edges can occur in two forms: *opposing edges* or *twisted
pairs*.

**Step 3: Eliminate adjacent opposing pairs**

Adjacent opposing pairs can be eliminated by foldiing them in and giving
them edges together.

**Step 4: Eliminate all but one vertext**

**Step 5: Collecting twisted pairs**

A twisted pair of edges labeled $a$ may be made adjacent by cutting
along the dotted line and regluing along the original edge $a$.

<figure>
<img src="images/clipboard-590326423.png" alt="Figure 6" />
<figcaption aria-hidden="true">Figure 6</figcaption>
</figure>

**Step 6: Collecting pairs of opposing pairs**

If steps 1 through 5 have been performed, then any opposing pairs must
occur in pairs.
