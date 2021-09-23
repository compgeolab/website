---
title: News
template: base.html
---

# {{ page.title }}

<p class="lead">
Lab news, updates, job postings, and more.
</p>

{# Create a list of pages from the news folder #}
{%- set news = [] %}
{%- for id, page in site.items() %}
  {%- if page.parent == "news" and id != "news/index" %}
    {%- do news.append(page) %}
  {%- endif %}
{%- endfor %}

<ul class="mt-4">
{%- for page in news|sort(attribute="date", reverse=True) %}
<li class="mb-2">
<span class="text-muted f-6">{{ page.date|replace("-", "/") }}:</span>
<a href="/{{ page.path }}">{{ page.title }}</a>
</li>
{%- endfor %}
</ul>
