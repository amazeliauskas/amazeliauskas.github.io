---
layout: page
title: Research
permalink: /projects/
description: 
nav: false
nav_order: 1
display_categories: [current, past]
horizontal: false
---

I am fascinated by the **far-from-equilibrium dynamics** and **thermalization processes** of strongly correlated systems.
My primary research interest is in studying the hot, dense nuclear matter--**quark-gluon plasma**--produced in high-energy particle colliders such as the **Large Hadron Collider (LHC)** at CERN and the
**Relativistic Heavy Ion Collider (RHIC)** at BNL. 
I have also worked on problems relevant for high-energy particle
physics and neutron star physics.
Recently, I have become interested in the remarkable similarities between non-equilibrium
physics in nuclear collisions  and **cold-atom experiments**.
Therefore, I am actively collaborating with
cold-atom experts to explore **interdisciplinary connections** between these two fields, which lie at opposite
ends of the energy scale. 

Below you can find more information about the research projects at my group.

<!-- pages/projects.md -->
<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="d-flex align-content-stretch justify-content-center flex-wrap no-gutters mx-n2 row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display projects without categories -->

{% assign sorted_projects = site.projects | sort: "importance" %}

  <!-- Generate cards for each project -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>


