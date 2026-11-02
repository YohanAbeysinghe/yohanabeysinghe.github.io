---
layout: page
title: Honors
permalink: /honors/
nav: true
nav_order: 3
---

<div class="compact-list-page">
{% assign categories = site.data.honors | group_by: 'category' %}
{% for category in categories %}
<section class="honors-section" aria-labelledby="{{ category.name | slugify }}">
  <h2 id="{{ category.name | slugify }}">{{ category.name }}</h2>
  <ul class="honors-list">
    {% assign awards = category.items | sort: 'year' | reverse %}
    {% for award in awards %}
      <li>
        {% if award.url %}<a href="{{ award.url }}">{{ award.name }}</a>{% else %}<strong>{{ award.name }}</strong>{% endif %}
        — {{ award.award }}, {{ award.year }}{% if award.location %} <span class="honor-location">· {{ award.location }}</span>{% endif %}
      </li>
    {% endfor %}
  </ul>
</section>
{% endfor %}
</div>
