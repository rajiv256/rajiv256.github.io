---
layout: blogpage
title: Blog
permalink: /blog/
defaults:
  - scope:
      path: ""
      type: posts
---
{% include base_path %}
<div class="wrapper">
  {% for post in site.posts %}
    <span>
      <a href="{{ site.url }}{{ post.permalink }}">
        {{ post.title }}
      </a>
    </span>
    <span class="post-date"> (<i>{{ post.date | date_to_string }}</i></span><i>{% include read-time.html %}</i>)
    <br>
  {% endfor %}
</div>
