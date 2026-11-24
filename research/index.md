---
title: Our research themes
template: base.html
---

{% import "macros.html" as macros %}

<div class="lead">

We focus our efforts on creating and applying new methods for solving **inverse
problems in geophysics** applied to **3D modeling and data processing**, mostly
for gravimetry and magnetometry (AKA **potential-field methods**). Below, you'll
find the main research themes that we pursue.

</div>


{%- macro paper_link(doi) %}
  <a href="../publications#{{ doi }}">{{ (site["publications/index"].publications.papers|selectattr("doi", "eq", doi)|list)[0].title }}</a>
{%- endmacro %}



{%- for tag, theme in page.themes|items %}
<section class="extra-space flow">
<h2 id="{{ tag }}">{{ theme.title }}</h2>

{{ theme.description }}

{{ macros.figure(src="../images/research/" + tag + ".webp", alt=theme.alt, caption=theme.caption) }}

<div class="callout">

Examples of our work on this theme:

{%- for theme_tag, papers in site["publications/index"].publications.papers|groupby("theme") %}
{%- if theme_tag == tag %}
{% for paper in papers %}
{%- if loop.index > 3 %}{% break %}{%- endif %}

* [{{ paper.title }}](../publications#{{ paper.doi }})

{% endfor %}
{%- endif %}
{%- endfor %}
</ul>

</div>

</section>
{%- endfor %}
