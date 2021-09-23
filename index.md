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

## About us

<div class="row gy-5 gx-5">
<div class="col-md-7">

The **CompGeoLab** is a research group based at the
[{{ config.location.university }}'s {{ config.location.school }}][uol].
We are experts in solving **inverse problems** in the field of **Geophysics**.
For example, determining the inner density distribution of the Earth from
measured disturbances in the Earth's gravity field.
These are the main tools used by geoscientists to **image the inside** of the
Earth and other planets.

We also specialize in building **open-source scientific software**.
Our team works on [several tools and projects](/software), both developing
tools in-house and contributing across the larger scientific ecosystem.

<div class="mt-5">
<a class="btn clab-button mb-4 me-2" href="/team">Meet the team</a>
<a class="btn clab-button-outline mb-4 me-2" href="/research">Our research</a>
<a class="btn clab-button-outline mb-4 me-2" href="/contact">Work with us!</a>
</div>

</div>
<div class="col-md-5">

{%- set caption = "Modelled density anomalies associated with iron-ore formations derived from observed gravity disturbances." %}
<img class="mb-5" src="/images/quadrilatero-ferrifero-density-model.png" alt="{{ caption }}" title="{{ caption }}">
{%- set caption = "Our software is built mostly with the Python and C languages." %}
<img src="/images/languages.svg" alt="{{ caption }}" title="{{ caption }}">

</div>
</div>

</div>
</div>
<div class="container-fluid">
<div class="container page-section">

## Lab updates

News, updates, job postings, and more:

{# Create a list of pages from the news folder #}
{%- set news = [] %}
{%- for id, item in site.items() %}
  {%- if item.parent == "news" and id != "news/index" %}
    {%- do news.append(item) %}
  {%- endif %}
{%- endfor %}

<ul class="mt-4">
{%- for item in (news|sort(attribute="date", reverse=True)|list)[:5] %}
<li>
<a href="/{{ item.path }}">{{ item.title }}</a>
<span class="text-muted fs-6">({{ item.date|replace("-", "/") }})</span>
</li>
{%- endfor %}
</ul>

<a class="btn btn-outline-primary mt-3" href="/news">More updates »</a>

</div>
</div>

[uol]: https://www.liverpool.ac.uk/earth-ocean-and-ecological-sciences/
