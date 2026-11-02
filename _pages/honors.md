---
layout: page
title: Honors
permalink: /honors/
description: Competition awards and international participation.
nav: true
nav_order: 3
---

{% assign categories = site.data.honors | group_by: 'category' %}
{% for category in categories %}

<section class="honors-section" aria-labelledby="{{ category.name | slugify }}">
  <h2 id="{{ category.name | slugify }}">{{ category.name }}</h2>
  <ul class="honors-list">
    {% for award in category.items %}
    <li>
      <span class="honor-year">{{ award.year }}</span>
      <div>
        <strong>{{ award.award }}</strong> · {% if award.url %}<a href="{{ award.url }}">{{ award.name }}</a>{% else %}{{ award.name }}{% endif %}
        {% if award.location %}<span class="honor-location">{{ award.location }}</span>{% endif %}
      </div>
    </li>
    {% endfor %}
  </ul>
</section>
{% endfor %}
