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

I am a Ph.D. student in Electrical and Computer Engineering at the [University of Maryland](https://ece.umd.edu/), where I work in the [GAMMA Lab](https://gamma.umd.edu/) under the supervision of [Prof. Dinesh Manocha](https://www.cs.umd.edu/people/dmanocha/). My research lies at the intersection of robotics, computer vision, and machine learning. I am interested in how intelligent systems can understand visual environments, reason about changes, and use that understanding to act in the physical world.

My current work focuses on robot navigation, vision-language-action models, and geometry-aware planning. I study how robots can learn navigation policies from visual experience and how geometric information can help guide their behavior in complex environments. I am also interested in world models, differentiable robotics, and the connections between learning, optimization, and control.

Alongside robotics, I work on vision-language models and multimodal video understanding. I am particularly interested in counterfactual reasoning and in evaluating whether models respond to changes in visual content or rely on information learned during training. My current work explores these questions through controlled edits to videos and their associated question-answering tasks, with an emphasis on detecting dataset contamination and understanding model behavior.

Before joining UMD, I was a Research Associate at the Mohamed bin Zayed University of Artificial Intelligence, working with Dr. Salman Khan. There, I developed machine learning methods for spatiotemporal air pollution forecasting, resulting in a first-author publication in _npj Clean Air_. My broader research experience includes diffusion-based video generation and EEG-based signal classification. During my research internship at the University of Sydney, I worked on protein structure prediction.

I received my B.Sc. (Hons) in Electronics and Telecommunication Engineering from the University of Moratuwa, Sri Lanka, graduating with First Class Honours. My undergraduate research explored interpretable EEG classification and the development of an ear-EEG acquisition device.

Mathematics has been an important part of my journey. I represented Sri Lanka at the International Mathematical Olympiad, where I received a bronze medal in 2017. I also received a bronze medal at the Asia Pacific Mathematics Olympiad and a gold medal at the Sri Lankan Physics Olympiad, and represented Sri Lanka at the International Physics Olympiad. At UMD, I was awarded the Dean’s Fellowship.

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
