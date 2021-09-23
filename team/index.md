---
title: Meet our team
template: base.html
---

<!-- This macro makes the list of people with links and icons -->
{%- macro make_list(people) %}
  <div class="row gy-3 gx-5 my-5">
    {%- for person in people %}
      <div class="col-12 col-sm-6 col-md-4 d-flex align-items-stretch">
        <div class="card">
          {%- if person.github is defined %}
            <img class="card-img-top" src="https://github.com/{{ person.github }}.png" alt="{{ person.name }}'s profile picture">
          {%- else %}
            <img class="card-img-top" src="/images/avatar-placeholder.jpg" alt="{{ person.name }}'s profile picture">
          {%- endif %}
          <div class="card-body text-center">
            <h3 class="card-title fs-4">{{ person.name }}</h3>
            <p class="card-text fs-6 mb-1 text-muted">{{ person.affiliation }}</p>
            <p class="card-text fs-6 mb-1 text-muted">{{ person.role }}</p>
            <ul class="fa-ul list-inline ms-0 fs-5 mb-1">
              {%- if person.github is defined %}
              <li class="list-inline-item">
                <a href="https://github.com/{{ person.github }}"
                   aria-label="GitHub" title="GitHub" target="_blank">
                   <i class="fab fa-github" aria-hidden="true"></i>
                </a>
              </li>
              {%- endif %}
              {%- if person.email is defined %}
              <li class="list-inline-item">
                <a href="mailto:{{ person.email }}"
                   aria-label="email" title="email" target="_blank">
                   <i class="fa fa-envelope-open" aria-hidden="true"></i>
                </a>
              </li>
              {%- endif %}
              {%- if person.orcid is defined %}
              <li class="list-inline-item">
                <a href="https://orcid.org/{{ person.orcid }}"
                   aria-label="ORCID" title="ORCID" target="_blank">
                   <i class="ai ai-orcid" aria-hidden="true"></i>
                </a>
              </li>
              <li class="list-inline-item">
                <a href="https://impactstory.org/u/{{ person.orcid }}"
                   aria-label="ImpactStory" title="ImpactStory" target="_blank">
                   <i class="ai ai-impactstory" aria-hidden="true"></i>
                </a>
              </li>
              {%- endif %}
              {%- if person.google_scholar is defined %}
              <li class="list-inline-item">
                <a href="{{ person.google_scholar }}"
                   aria-label="Google Scholar" title="Google Scholar" target="_blank">
                   <i class="ai ai-google-scholar" aria-hidden="true"></i>
                </a>
              </li>
              {%- endif %}
              {%- if person.researchgate is defined %}
              <li class="list-inline-item">
                <a href="{{ person.researchgate }}"
                   aria-label="ResearchGate" title="ResearchGate" target="_blank">
                   <i class="ai ai-researchgate" aria-hidden="true"></i>
                </a>
              </li>
              {%- endif %}
              {%- if person.cv is defined %}
              <li class="list-inline-item">
                <a href="{{ person.cv }}"
                   aria-label="CV" title="CV" target="_blank">
                   <i class="ai ai-cv" aria-hidden="true"></i>
                </a>
              </li>
              {%- endif %}
              {%- if person.website is defined %}
              <li class="list-inline-item">
                <a href="{{ person.website }}"
                   aria-label="Website" title="Website" target="_blank">
                   <i class="fa fa-external-link-square-alt" aria-hidden="true"></i>
                </a>
              </li>
              {%- endif %}
            </ul>
          </div>
        </div>
      </div>
    {%- endfor %}
  </div>
{%- endmacro %}


<!-- This is where the page source starts -->

# {{ page.title }}

<p class="lead">
We are an international group of researchers joined by a shared passion for
geoscience and helping our peers by making free high-quality tools.
</p>

{{ make_list(page.current) }}

<hr class="mb-5">

## Collaborators

Research is never done in a vacuum! We are proud to collaborate with
world-leading researchers:

{{ make_list(page.collaborators) }}

<hr class="mb-5">

## Alumni

People who passed through the lab and have since moved on:

{{ make_list(page.alumni) }}
