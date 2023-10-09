---
title: Meet our team
template: base.html
---

{%- import "macros.html" as macros %}

# {{ page.title }}

<div class="lead">

We are an international group of researchers joined by a shared passion for
geoscience and open-source.

</div>

## Team members

The core team working across our research themes:

{%- for person in page.people.current %}
  <div class="profile">
    <img src="https://github.com/{{ person.github }}.png">
    <ul role="list">
      <li>{{ person.name }}</li>
    </ul>
  </div>
{%- endfor %}


## Collaborators

Research is never done in a vacuum! We are proud to collaborate with
world-leading researchers:



## Alumni

These are some of the people who passed through the lab and have since moved on
(only those who have added themselves):


