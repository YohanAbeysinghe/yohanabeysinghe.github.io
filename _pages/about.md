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

I am a Ph.D. student in Electrical and Computer Engineering at the [University of Maryland](https://ece.umd.edu/), working in the [GAMMA Lab](https://gamma.umd.edu/) under the supervision of [Prof. Dinesh Manocha](https://www.cs.umd.edu/people/dmanocha/). My research lies at the intersection of robotics, computer vision, and machine learning.

I study how robots can learn from visual experience to understand and navigate complex environments, with a focus on vision-language-action models and geometry-aware planning. I also work on multimodal video understanding and counterfactual reasoning, exploring whether vision-language models respond to visual changes or rely on memorized information.

Before joining UMD, I was a Research Associate at the Mohamed bin Zayed University of Artificial Intelligence, working with Dr. Salman Khan on air pollution forecasting, with a first-author publication in _npj Clean Air_. I also completed a research internship at the University of Sydney on protein structure prediction. I received my B.Sc. (Hons) in Electronics and Telecommunication Engineering from the University of Moratuwa, Sri Lanka, graduating with First Class Honours.

I represented Sri Lanka at the International Mathematical Olympiad, receiving a bronze medal in 2017, and at the International Physics Olympiad. I also received a bronze medal at the Asia Pacific Mathematics Olympiad, a gold medal at the Sri Lankan Physics Olympiad, and the Dean’s Fellowship at UMD.

</div>
</div>

{% if site.data.availability.enabled %}

<aside class="availability" aria-label="Internship availability">{{ site.data.availability.text }}</aside>
{% endif %}

<section aria-labelledby="interests" markdown="1">
<h2 id="interests">Interests</h2>

Robot Learning, Robot Navigation, Computer Vision, Vision-Language Models, Counterfactual Reasoning, Vision-Language-Action Models, Geometry, Optimization, Control, Mathematics, Chess, Reading

</section>

<section aria-labelledby="contact" markdown="1">
<h2 id="contact">Contact</h2>

<p><strong>Email:</strong> {{ site.data.socials.email | replace: '@', '_AT_' | replace: '.', '_DOT_' }}</p>

<nav class="profile-links" aria-label="CV and profiles">
  <a href="{{ site.data.socials.cv_pdf | relative_url }}">CV</a>
  <a href="https://scholar.google.com/citations?user={{ site.data.socials.scholar_userid }}&amp;hl=en">Google Scholar</a>
  <a href="https://github.com/{{ site.data.socials.github_username }}">GitHub</a>
  <a href="https://www.linkedin.com/in/{{ site.data.socials.linkedin_username }}/">LinkedIn</a>
</nav>
</section>
