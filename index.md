---
custom_page_title: Computer-Oriented Geoscience Lab
banner_title: "Geophysical research <br> powered by open-source software"
banner_subtitle: |
  At the <strong>Computer-Oriented Geoscience Lab</strong>, we design
  state-of-the-art computational tools for geophysical data.
  <strong>Source code included.</strong>
no_container: true
template: base.html
---

<div class="container-fluid" style="background-color: var(--bs-gray-200);">
<div class="container page-section">

## About

The **CompGeoLab** is a research group based at the
[{{ config.location.university }}'s {{ config.location.school }}][uol].
We are experts in solving **inverse problems** in the field of **Geophysics**.
For example, determining the inner density distribution of the Earth from
measured disturbances in the Earth's gravity field.
These are the main tools used by geoscientists to **image the inside** of the
Earth and other planets.

SOMETHING ABOUT SOFTWARE.

<div class="mt-4">
<a class="btn clab-button mb-4 me-2" href="/research">Our research</a>
<a class="btn clab-button mb-4" href="/people">Meet the team</a>
</div>

</div>
</div>
<div class="container-fluid">
<div class="container page-section">

## Lab updates

{# Create a list of pages from the news folder #}
{%- set news = [] %}
{%- for id, page in site.items() %}
  {%- if page.parent == "news" and id != "news/index" %}
    {%- do news.append(page) %}
  {%- endif %}
{%- endfor %}

<ul class="mt-4">
{%- for page in (news|sort(attribute="date", reverse=True)|list)[:5] %}
<li class="mb-2">
<span class="text-muted f-6">{{ page.date|replace("-", "/") }}:</span>
<a href="/{{ page.path }}">{{ page.title }}</a>
</li>
{%- endfor %}
</ul>

[Past updates »](/news)

</div>
</div>

[uol]: https://www.liverpool.ac.uk/earth-ocean-and-ecological-sciences/
