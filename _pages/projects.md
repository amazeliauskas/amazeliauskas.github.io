---
layout: page
title: Research
permalink: /projects/
description: >
    I am fascinated by many-body physics emerging from interactions of elementary particles in a hot and dense nuclear matter created in high-energy hadron collisions at particle accelerators like LHC (CERN) and RHIC (BNL). I am trying to understand the properties of the new state of nuclear matter—the quark-gluon plasma (QGP), which is formed at extreme temperature and density. Outside hadron collisions, such conditions can be found only at the beginning of the Universe and in violent neutron start mergers.

    Recently I have been particularly interested in the formation of the quark-gluon plasma at the earliest stages of the collision. I use a weakly coupled kinetic theory of quarks and gluons to perform state-of-the-art simulations elucidating the phenomena of equilibration and fluid-like behaviour of relatively small number of particles interacting via the strong force. I have also worked on the hydrodynamic descriptions of quark-gluon plasma expansion and I am actively working on improving the conversion from fluid fields to measurable hadrons at late stages of the collision.
nav: false
nav_order: 1
display_categories: [active, inactive]
horizontal: false
---

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


