---
layout: blogpage
title: Blog
permalink: /blog/
defaults:
  # _posts
  - scope:
      path: ""
      type: posts
---

<div class="wrapper">
  {% for post in site.posts %}
    <h4>
      <a href="{{ site.baseurl }}/{{ post.permalink }}">
        {{ post.title }}
      </a>
    </h4>
    <span class="post-date">{{ post.date | date_to_string }}</span>
    {% if post.tags %} |
    {% for tag in post.tags %}
    <a href="{{ site.baseurl }}{{ site.tag_page }}#{{ tag | slugify }}" class="post-tag">{{ tag }}</a>
    {% endfor %}
    {% endif %}
  {% endfor %}
<!--</div>-->

<!-- <div class="pagination">
  {% if paginator.next_page %}
    <a class="pagination-item older" href="{{ site.baseurl }}/blog/page{{ paginator.next_page }}">Older</a>
  {% else %}
    <span class="pagination-item older">Older</span>
  {% endif %}
  {% if paginator.previous_page %}
    {% if paginator.page == 2 %}
      <a class="pagination-item newer" href="{{ site.baseurl }}/blog/">Newer</a>
    {% else %}
      <a class="pagination-item newer" href="{{ site.baseurl }}/blog/page{{ paginator.previous_page }}">Newer</a>
    {% endif %}
  {% else %}
    <span class="pagination-item newer">Newer</span>
  {% endif %}
</div> -->
