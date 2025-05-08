---
layout: homepage
---

## Lil' Intro

Good tidings! This is Rajiv, a PhD student in the CompSci department at
Duke. Here, I work with <a href="https://users.cs.duke.edu/~reif/">Prof.
John Reif</a> in the field of Natural Computing
(<a href="https://www.dna.caltech.edu/DNAresearch_perspective.html">huh?</a>).
Some sane people refer to this field as DNA Computing, as we use
synthetic DNA molecules to create molecular-scale computational devices.
Can we make them to be modular, self-sufficient systems? That is the
question. When I am not worried about my future, I like to play
chess/badminton, read classical literature, and watch movies. I
occasionally write poems and stories
<a href="https://rajivteja.wordpress.com/"> here</a>.

**PSA:** If you are a prospective graduate student applying for PhD
programs in Computer Science, I highly recommend reading
"<a href="https://www.cs.cmu.edu/~harchol/gradschooltalk.pdf">The Gradschool Talk by Prof. Mor Harchol-Balter</a>".

## Research Interests

-   Biomolecular Computing: What kind of information processing
    capabilities does a bag of reacting biomolecules (e.g., dna, rna)
    possess?
-   Biochemical Learning: Can we make these systems to be adaptive
    and operate autonomously?

## Timeline

-   **[Jun 2024]**: Paper published in the Royal Society Interface
    journal
    <a href="https://royalsocietypublishing.org/doi/10.1098/rsif.2024.0053">[Paper]</a>
-   **[Aug 2022]**: Awarded the GPNANO fellowship for the Fall 2022
    semester
-   **[May 2022]**: Defended the Research Initiation Project proposal
-   **[Aug 2021]**: Joined the Computer Science PhD program at Duke
    University, Durham NC
-   **[Mar 2020]**: Joined Google Research as a contract employee
    through Optimum
-   **[Dec 2018]**: Left PayPal and joined Kenome.io
-   **[Aug 2017]**: Joined PayPal
-   **[Oct 2017]**: Paper accepted to MIKE 2017
-   **[Jul 2017]**: Received my undergraduate degree from the CS
    department at IIT Madras
-   **[Apr 2017]**: Submitted my undergraduate thesis on [A Unikernel
    Webserver in Rust](https://rajiv256.github.io/projects/ouros/)

<h2 id="publications" style="margin: 2px 0px -15px;">Publications</h2>

<div class="publications">
<ol class="bibliography">

{% for link in site.data.publications.main %}

<li>
<div class="pub-row">
  <div class="col-sm-3 abbr" style="position: relative;padding-right: 15px;padding-left: 15px;">
    {% if link.image %} 
    <img src="{{ link.image }}" class="teaser img-fluid z-depth-1" style="width=100;height=40%">
    {% if link.conference_short %} 
    <abbr class="badge">{{ link.conference_short }}</abbr>
    {% endif %}
    {% endif %}
  </div>
  <div class="col-sm-9" style="position: relative;padding-right: 15px;padding-left: 20px;">
      <div class="title"><a href="{{ link.pdf }}">{{ link.title }}</a></div>
      <div class="author">{{ link.authors }}</div>
      <div class="periodical"><em>{{ link.conference }}</em>
      </div>
    <div class="links">
      {% if link.pdf %} 
      <a href="{{ link.pdf }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">PDF</a>
      {% endif %}
      {% if link.code %} 
      <a href="{{ link.code }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">Code</a>
      {% endif %}
      {% if link.page %} 
      <a href="{{ link.page }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">Project Page</a>
      {% endif %}
      {% if link.bibtex %} 
      <a href="{{ link.bibtex }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">BibTex</a>
      {% endif %}
      {% if link.notes %} 
      <strong> <i style="color:#e74d3c">{{ link.notes }}</i></strong>
      {% endif %}
      {% if link.others %} 
      {{ link.others }}
      {% endif %}
    </div>
  </div>
</div>
</li>
<br>

{% endfor %}

</ol>
</div>

