---
layout: album
title: Photo Album
---

<!-- <section class="projects-filter">
  <ul>
    <li><a href="#">Notes</a></li>
    <li><a href="#">Patrimoine</a></li>
    <li><a href="#">Logements</a></li>
    <li><a href="#">Ateliers & bureaux</a></li>
    <li><a href="#">Équipement</a></li>
    <li><a href="#">Architectures flottantes</a></li>
  </ul>
</section> -->

<section class="photo-grid">
  {% for project in site.data.projects.featured %}
    <div class="pcard">
      <a href="/images/{{ project.image | relative_url}}.webp" data-fancybox="gallery">
        <picture>
          <source srcset="/images/{{ project.image | relative_url}}.webp" type="image/webp">
          <img src="/images/{{ project.image | relative_url}}.jpg" alt="Gallery Image" loading="lazy">
        </picture>
        <div class="pcard-description">
          <span class="left"> {{ project.title }} </span> <span class="right"> {{ project.description }} </span> 
        </div>
      </a>
    </div>
  {% endfor %}
</section>


