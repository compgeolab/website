---
title: Meet our team
template: base.html
---

{%- import "macros.html" as macros %}

<div class="lead">

We are a group of scientists joined by a shared passion for geoscience, problem
solving, open science, and software engineering.

</div>

{{ macros.figure("../images/compgeolab-group-photo-2024-08-12.jpg", caption="CompGeoLab members (as of August 2024) in front of the IAG building at Universidade de São Paulo. From left to right: Yago, Santiago, Ellen, Leo, India, Arthur, Gelson, Gabriel. This was the first time ever that our whole team was physically in the same place!", alt="Group of men and women standing shoulder-to-shoulder and smiling in the sunlight in front of a building entrance, with concrete pillars and stairs leading into glass doors with IAG logo on them." ) }}

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
        <li>Links:
          {%- set links = [] -%}
          {%- if person.github is defined -%}
            {%- do links.append(("https://github.com/" + person.github, "GitHub")) -%}
          {%- endif -%}
          {%- if person.lattes is defined -%}
            {%- do links.append(("https://lattes.cnpq.br/" + person.lattes, "Lattes")) -%}
          {%- endif -%}
          {%- if person.researchgate is defined -%}
            {%- do links.append(("https://www.researchgate.net/profile/" + person.researchgate, "ResearchGate")) -%}
          {%- endif -%}
          {%- if person.google_scholar is defined -%}
            {%- do links.append(("http://scholar.google.com/citations?user=" + person.google_scholar, "Google Scholar")) -%}
          {%- endif -%}
          {%- for url, title in links %}
            <a href="{{ url }}" target="_blank">{{ title }}</a>{%- if
            not loop.last %} / {%- endif %}
          {%- endfor %}
        </li>
        {%- if person.project is defined %}
          <li>Project: <span class="text-muted">"{{ person.project }}"</span></li>
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
