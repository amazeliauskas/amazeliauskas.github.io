---
layout: page
permalink: /publications/
title: Publications
description:
nav: false
nav_order: 4
---

For up to date publication list see [INSPIRE](https://inspirehep.net/authors/1503337?ui-citation-summary=true&ui-exclude-self-citations=true)

<div class="row text-center my-4">
  <div class="col">
    <h3 class="mb-0">{% inspirehep_author_summary papers %}</h3>
    <p class="text-muted mb-0">papers</p>
  </div>
  <div class="col">
    <h3 class="mb-0">{% inspirehep_author_summary papers_published %}</h3>
    <p class="text-muted mb-0">published</p>
  </div>
  <div class="col">
    <h3 class="mb-0">{% inspirehep_author_summary citations %}</h3>
    <p class="text-muted mb-0">citations</p>
  </div>
  <div class="col">
    <h3 class="mb-0">{% inspirehep_author_summary citations exclude_self %}</h3>
    <p class="text-muted mb-0">citations, excl. self</p>
  </div>
  <div class="col">
    <h3 class="mb-0">{% inspirehep_author_summary h_index %}</h3>
    <p class="text-muted mb-0">h-index</p>
  </div>
</div>

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

{% bibliography %}

</div>
