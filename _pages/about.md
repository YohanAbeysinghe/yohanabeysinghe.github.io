---
layout: about
title: About
permalink: /
profile: false
selected_papers: false
social: false
announcements:
  enabled: false
latest_posts:
  enabled: false
---

<div class="about-intro" markdown="1">
<figure class="portrait-frame">
  <img class="portrait" src="{{ '/images/yohan_headshot.jpeg' | relative_url }}" alt="Portrait of Yohan Abeysinghe" width="220" height="220" fetchpriority="high">
</figure>
<div class="intro-copy" markdown="1">

<h2 class="intro-heading">About</h2>

I am a PhD student in Electrical and Computer Engineering at the [University of Maryland](https://ece.umd.edu/), working with [Prof. Dinesh Manocha](https://www.cs.umd.edu/people/dmanocha/) in the [GAMMA Lab](https://gamma.umd.edu/). My research focuses on **robot learning and multimodal AI**, with an emphasis on using geometry and physical structure to build reliable navigation policies.

Previously, I was a Research Associate at MBZUAI and a research intern at the University of Sydney. I received my B.Sc. (Hons), with First Class Honours, from the University of Moratuwa.

<nav class="profile-links" aria-label="Contact and profiles">
  <a href="mailto:{{ site.data.socials.email }}">Email</a>
  <a href="{{ site.data.socials.cv_pdf | relative_url }}">CV</a>
  <a href="https://scholar.google.com/citations?user={{ site.data.socials.scholar_userid }}&amp;hl=en">Google Scholar</a>
  <a href="https://github.com/{{ site.data.socials.github_username }}">GitHub</a>
  <a href="https://www.linkedin.com/in/{{ site.data.socials.linkedin_username }}/">LinkedIn</a>
</nav>
</div>
</div>

{% if site.data.availability.enabled %}

<aside class="availability" aria-label="Internship availability">{{ site.data.availability.text }}</aside>
{% endif %}

<nav class="about-page-links" aria-label="Explore my work and background">
  <a href="{{ '/publications/' | relative_url }}">Publications <span aria-hidden="true">→</span></a>
  <a href="{{ '/experience/' | relative_url }}">Experience &amp; education <span aria-hidden="true">→</span></a>
</nav>
