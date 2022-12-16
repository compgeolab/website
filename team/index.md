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

<section class="my-5">

## Team members

The core team working across our [themes and projects](../research):

{{ macros.make_people_list(page.people.current) }}

</section>

<hr>

<section class="my-5">

## Collaborators

Research is never done in a vacuum! We are proud to collaborate with
world-leading researchers:

{{ macros.make_people_list(page.people.collaborators) }}

</section>

<hr>

<section class="mt-5">

## Alumni

People who passed through the lab and have since moved on:

{{ macros.make_people_list(page.people.alumni, prefix="alum-") }}

</section>
