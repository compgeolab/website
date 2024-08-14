---
title: Meet our team
template: base.html
---

{%- import "macros.html" as macros %}

<div class="lead">

We are an international group of researchers joined by a shared passion for
geoscience and open-source.

</div>

{{ macros.figure("../images/compgeolab-group-photo-2024-08-12.jpg", caption="CompGeoLab members (as of August 2024) in front of the IAG building at Universidade de São Paulo. From left to right: Yago, Santiago, Ellen, Leo, India, Arthur, Gelson, Gabriel.", alt="Group of men and women standing shoulder-to-shoulder and smiling in the sunlight in front of a building entrance, with concrete pillars and stairs leading into glass doors with IAG logo on them." ) }}

{%- macro profiles(people) %}
{# Function for generating the profiles of a list of people #}
{%- for person in people %}
  {%- if person.id is defined %}
    {%- set id=person.id %}
  {%- else %}
    {%- set id=person.github %}
  {%- endif %}
  <div class="profile">
    <div class="profile-info flow">
      <h3 id="{{ id }}">
        {{ person.name }}
        {%- if person.pronouns is defined %}
          <span class="font-normal">({{ person.pronouns }})</span>
        {%- endif %}
      </h3>
      <ul role="list">
        <li><span class="text-bold">{{ person.role }}</span></li>
        <li>{{ person.affiliation }}</li>
        {%- if person.email is defined %}
          <li>Email: <a href="mailto:{{ person.email }}" target="_blank">{{ person.email }}</a></li>
        {%- endif %}
        {%- if person.orcid is defined %}
          <li>ORCID: <a href="https://orcid.org/{{ person.orcid }}" target="_blank">{{ person.orcid }}</a></li>
        {%- endif %}
        {%- if person.website is defined %}
          <li>Website: <a href="{{ person.website }}" target="_blank">{{ person.website[8:] }}</a></li>
        {%- endif %}
        {%- if person.project is defined %}
          <li>Project: <span class="text-muted">{{ person.project }}</span></li>
        {%- endif %}
      </ul>
      <ul class="list-inline font-large" role="list">
        {%- if person.github is defined %}
          <li><a href="https://github.com/{{ person.github }}" target="_blank"><i class="fab fa-github" aria-label="GitHub" title="GitHub"></i></a></li>
        {%- endif %}
        {%- if person.lattes is defined %}
          <li><a href="https://lattes.cnpq.br/{{ person.lattes }}" target="_blank"><i class="ai ai-lattes" aria-label="Currículo Lattes" title="Currículo Lattes"></i></a></li>
        {%- endif %}
        {%- if person.google_scholar is defined %}
          <li><a href="{{ person.google_scholar }}" target="_blank"><i class="ai ai-google-scholar" aria-label="Google Scholar" title="Google Scholar"></i></a></li>
        {%- endif %}
        {%- if person.orcid is defined %}
          <li><a href="https://impactstory.org/u/{{ person.orcid }}" target="_blank"><i class="ai ai-impactstory" aria-label="ImpactStory" title="ImpactStory"></i></a></li>
        {%- endif %}
        {%- if person.researchgate is defined %}
          <li><a href="{{ person.researchgate }}" target="_blank"><i class="ai ai-researchgate" aria-label="ResearchGate" title="ResearchGate"></i></a></li>
        {%- endif %}
      </ul>
    </div>
    {%- if person.picture is defined %}
      {%- set picture = person.picture %}
    {%- else %}
      {%- set picture = "https://github.com/" + person.github + ".png" %}
    {%- endif %}
    <img src="{{ picture }}" alt="Profile picture of {{ person.name }}">
  </div>
{%- endfor %}
{%- endmacro %}



## Team members

The core team working across our research themes:

{{ profiles(page.people.current) }}

## Collaborators

Research is never done in a vacuum! We are proud to collaborate with
world-leading researchers:

{{ profiles(page.people.collaborators) }}

## Alumni

These are some of the people who passed through the lab and have since moved on
(only those who have added themselves):

{{ profiles(page.people.alumni) }}
