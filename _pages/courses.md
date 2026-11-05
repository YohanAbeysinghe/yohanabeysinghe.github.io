---
layout: page
title: Courses
permalink: /courses/
nav: true
nav_order: 4
---

<div class="compact-list-page">
<section aria-labelledby="courses-taken">
  <h2 id="courses-taken">Courses taken</h2>
  <ul class="coursework-list">
    {% for course in site.data.courses.coursework %}
      <li>
        {% if course.course_url %}<a href="{{ course.course_url }}">{{ course.code }} — {{ course.title }}</a>{% else %}{{ course.code }} — {{ course.title }}{% endif %} <span class="course-term">({{ course.semester }})</span>{% if course.status %} <span class="course-status">· {{ course.status }}</span>{% endif %}
        {% assign notes_url = course.notes_url | default: '' | strip %}
        {% if notes_url != empty %}<a class="course-notes" href="{{ notes_url | relative_url | escape }}" aria-label="Personal notes for {{ course.code | escape }}, {{ course.semester | escape }}">notes</a>{% endif %}
      </li>
    {% endfor %}
  </ul>
</section>

<section aria-labelledby="courses-taught">
  <h2 id="courses-taught">Courses taught (TA)</h2>
  <ul class="coursework-list">
    {% for course in site.data.courses.teaching %}
      <li>
        {{ course.code }} — {{ course.title }} <span class="course-term">({{ course.semester }})</span>, with <a href="{{ course.instructor_url }}">Prof. {{ course.instructor }}</a>.
        {% assign notes_url = course.notes_url | default: '' | strip %}
        {% if notes_url != empty %}<a class="course-notes" href="{{ notes_url | relative_url | escape }}" aria-label="Personal notes for {{ course.code | escape }}, {{ course.semester | escape }}">notes</a>{% endif %}
      </li>
    {% endfor %}
  </ul>
</section>
</div>
