---
title: Publications
template: base.html
---

<div class="lead">

We strive to make all our publications **accessible** and **reproducible**.
In this list, you'll always find links to open-access material, including
preprints, source code, and data.

</div>


{% macro publication_list(articles) %}
{% if articles %}
<ul role="list" class="flow">
{%- for article in articles %}
  <li id="{{ article.doi }}">
  <span class="font-small">[{{ "{:02d}".format(loop.revindex) }}]</span>
  <strong>{{ article.title }}.</strong>
  {{ article.authors }} ({{ article.year }}).
  <em>{{ article.journal }}</em>.
  DOI: <a target="_blank" href="https://doi.org/{{ article.doi }}">{{ article.doi }}</a>.
  {%- if article.preprint is defined %}
  Preprint: <a target="_blank" href="https://doi.org/{{ article.preprint }}">{{ article.preprint }}</a>.
  {%- endif %}
  {%- if article.data is defined %}
  Data: <a target="_blank" href="https://doi.org/{{ article.data }}">{{ article.data }}</a>.
  {%- endif %}
  {%- if article.github is defined %}
  Code: <a target="_blank" href="https://github.com/{{ article.github }}">{{ article.github }}</a>.
  {%- endif %}
</li>
{%- endfor %}
</ul>
{% else %}
<p><strong>None for now. Check back later!</strong></p>
{% endif %}
{% endmacro %}


## Preprints

These publications have not yet been peer-reviewed:

{{ publication_list(page.publications.preprints) }}

## Papers

These publications have gone through peer-review and have been published in an
academic journal:

{{ publication_list(page.publications.papers) }}
