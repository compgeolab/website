---
title: Meet our team
template: base.html
---

{%- import "macros.html" as macros %}

# {{ page.title }}

<p class="lead">
We are an international group of researchers joined by a shared passion for
geoscience and helping our peers by making free high-quality tools.
</p>

{{ macros.make_people_list(page.people.current) }}

<hr class="mb-5">

## Collaborators

Research is never done in a vacuum! We are proud to collaborate with
world-leading researchers:

{{ macros.make_people_list(page.people.collaborators) }}

<hr class="mb-5">

## Alumni

People who passed through the lab and have since moved on:

{{ macros.make_people_list(page.people.alumni) }}
