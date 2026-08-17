---
layout: blogpage
title: Blog
permalink: /blog/
defaults:
  - scope:
      path: ""
      type: posts
---
<div class="post-list">
{% for post in site.posts %}
  {% assign words = post.content | number_of_words %}
  <article class="post-entry">
    <div class="post-entry__meta">
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%b %-d, %Y' }}</time>
      <span>{% if words < 360 %}1 min{% else %}{{ words | divided_by: 180 }} min{% endif %}</span>
    </div>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    <a class="post-entry__link" href="{{ post.url | relative_url }}" aria-label="Read {{ post.title }}">Read essay <span aria-hidden="true">→</span></a>
  </article>
{% endfor %}
</div>
