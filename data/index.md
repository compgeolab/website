---
title: Data & Models
template: base.html
---

{% from "macros.html" import figure, video %}

# {{ page.title }}

<p class="lead">
The datasets and models produced along the course of our research are
<strong>open-access</strong>, available for free under permissive licenses
(usually the
<a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution</a>
license).
Below is a curated list of datasets and models generated or compiled by the
group.
</p>

{%- for data in page.datasets %}
  <div class="row mt-5 gy-5 gx-5">
  <div class="col-md-7">
    <h2>{{ data.title }}</h2>
    <p>{{ data.description }}</p>
    <a class="btn btn-primary mb-2 me-3" target="_blank" href="https://doi.org/{{ data.doi }}">
      <i class="fa fa-download me-1" aria-hidden="true"></i> Download
    </a>
    <a class="btn btn-outline-primary mb-2 me-3" target="_blank" href="https://github.com/{{ data.repository }}">
      <i class="fab fa-github me-1" aria-hidden="true"></i> Source code
    </a>
    <a target="_blank" class="btn btn-outline-primary mb-2 me-2" href="{{ data.license_url }}">
      <i class="fa fa-gavel me-1" aria-hidden="true"></i> License: {{ data.license }}
    </a>
  </div>
  <div class="col-md-5 {{ loop.cycle('', 'order-md-first') }}">
    {{ figure(src=data.image, caption=data.caption) }}
  </div>
  </div>
{%- endfor %}
