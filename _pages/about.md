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

I am a second year Ph.D. student in Electrical and Computer Engineering at the [University of Maryland](https://ece.umd.edu/), working in the [GAMMA Lab](https://gamma.umd.edu/) under the supervision of [Prof. Dinesh Manocha](https://www.cs.umd.edu/people/dmanocha/). My research lies at the intersection of robotics, computer vision, and machine learning.

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

<p><strong>Email:</strong> <a href="mailto:{{ site.data.socials.email }}">{{ site.data.socials.email }}</a></p>

<nav class="profile-links" aria-label="Social profiles">
  <a href="https://scholar.google.com/citations?user={{ site.data.socials.scholar_userid }}&amp;hl=en" aria-label="Google Scholar" title="Google Scholar">
    <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 0 0 9.75l4.8 3.9a8 8 0 1 1 14.4 0L24 9.75ZM12 8a6 6 0 1 0 0 12 6 6 0 0 0 0-12Z"/></svg>
  </a>
  <a href="https://github.com/{{ site.data.socials.github_username }}" aria-label="GitHub" title="GitHub">
    <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 .3a12 12 0 0 0-3.8 23.4c.6.1.8-.3.8-.6v-2.2c-3.3.7-4-1.4-4-1.4-.5-1.4-1.3-1.7-1.3-1.7-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.5.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0C17.4 5.1 18.4 5.4 18.4 5.4c.6 1.7.2 2.9.1 3.2.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.2c0 .3.2.7.8.6A12 12 0 0 0 12 .3Z"/></svg>
  </a>
  <a href="https://www.linkedin.com/in/{{ site.data.socials.linkedin_username }}/" aria-label="LinkedIn" title="LinkedIn">
    <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20.45 0H3.55A3.55 3.55 0 0 0 0 3.55v16.9A3.55 3.55 0 0 0 3.55 24h16.9A3.55 3.55 0 0 0 24 20.45V3.55A3.55 3.55 0 0 0 20.45 0ZM7.1 20.45H3.55V9H7.1ZM5.33 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12Zm15.12 13.02H16.9v-5.57c0-1.33-.03-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.36V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.26 2.37 4.26 5.45Z"/></svg>
  </a>
</nav>
</section>
