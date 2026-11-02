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
  <ul class="course-list">
    {% for course in site.data.courses.taken %}
      <li><strong>{{ course.code }}</strong> — {{ course.title }}</li>
    {% endfor %}
  </ul>
</section>

<section aria-labelledby="in-progress">
  <h2 id="in-progress">In progress</h2>
  <ul class="course-list">
    {% for course in site.data.courses.in_progress %}
      <li><strong>{{ course.code }}</strong> — {{ course.title }} <span class="course-term">({{ course.semester }})</span></li>
    {% endfor %}
  </ul>
</section>

<section aria-labelledby="courses-taught">
  <h2 id="courses-taught">Courses taught (TA)</h2>
  <ul class="course-list">
    {% for course in site.data.courses.teaching %}
      <li>
        <strong>{{ course.code }}</strong> — {{ course.title }}
        <span class="course-instructors">With {% for instructor in course.instructors %}<a href="{{ instructor.url }}">Prof. {{ instructor.name }}</a>{% unless forloop.last %}, {% endunless %}{% endfor %}.</span>
      </li>
    {% endfor %}
  </ul>
</section>
</div>
