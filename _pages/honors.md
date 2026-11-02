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
    {% assign competitions = category.items | group_by: 'name' %}
    {% for competition in competitions %}
      {% assign linked_award = competition.items | where_exp: 'award', 'award.url' | first %}
      {% assign results = competition.items | group_by: 'award' %}
      <li>
        {% if linked_award %}<a href="{{ linked_award.url }}">{{ competition.name }}</a>{% else %}<strong>{{ competition.name }}</strong>{% endif %}
        — {% for result in results %}{{ result.name }} ({{ result.items | map: 'year' | join: ', ' }}){% unless forloop.last %}; {% endunless %}{% endfor %}
      </li>
    {% endfor %}
  </ul>
</section>
{% endfor %}
</div>
