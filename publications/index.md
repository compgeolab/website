---
title: Publications
template: base.html
---

<div class="lead">

We strive to make all our publications **accessible** and **reproducible**. In
this list, you'll always find links to open-access material, including source
code and data.

</div>


{% macro publication_list(articles) %}
<ul role="list" class="flow">
{%- for article in articles %}
  <li><strong>{{ article.title }}.</strong> {{ article.authors }} ({{ article.year }}). <em>{{ article.journal }}</em>. DOI: <a target="_blank" href="https://doi.org/{{ article.doi }}">{{ article.doi }}</a>. Data: <a target="_blank" href="https://doi.org/{{ article.data }}">{{ article.data }}</a>. Code: <a target="_blank" href="https://github.com/{{ article.repository }}">{{ article.repository }}</a>.</li>
{%- endfor %}
</ul>
{% endmacro %}


## Preprints

These publications have not yet been peer-reviewed:

{{ publication_list(page.publications.preprints) }}

## Papers

These publications have gone through peer-review and have been published in an
academic journal:

{{ publication_list(page.publications.papers) }}
