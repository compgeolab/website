---
title: Meet our team
template: base.html
---

{%- import "macros.html" as macros %}

# {{ page.title }}

<p class="lead">
We are an international group of researchers joined by a shared passion for
geoscience and open-source.
</p>

<section>

## Team members

The core team working across our research themes:

{{ macros.make_people_list(page.people.current) }}

</section>

<hr class="section-separator">

<section>

## Collaborators

Research is never done in a vacuum! We are proud to collaborate with
world-leading researchers:

{{ macros.make_people_list(page.people.collaborators) }}

</section>

<hr class="section-separator">

<section>

## Alumni

These are some of the people who passed through the lab and have since moved on
(only those who have added themselves):

{{ macros.make_people_list(page.people.alumni, prefix="alum-") }}

</section>
