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
        {{ course.code }} — {{ course.title }} <span class="course-term">({{ course.semester }})</span>{% if course.status %} <span class="course-status">· {{ course.status }}</span>{% endif %}
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
      </li>
    {% endfor %}
  </ul>
</section>
</div>
