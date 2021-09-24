---
title: Publications
template: base.html
---

{%- import "macros.html" as macros %}

# {{ page.title }}

<p class="lead">
These are some of the publications involving our team members. All have PDF
versions <strong>freely available</strong> (i.e., self-archived, open-access,
or as preprints/postprints). Most also include links to source code and data.
</p>

{{ macros.make_publication_list(page.papers) }}
