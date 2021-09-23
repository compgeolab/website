---
title: Data & Models
template: base.html
---

# {{ page.title }}

<p class="lead">
Along the course of our research, we often produce open-access datasets and
models.
These products are available for free under permissive licenses (usually the
<a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution</a>
license).
Below is a curated list of datasets and models generated or compiled by the
group.
</p>

<div class="row mt-5 gy-5 gx-5">
<div class="col-md-7">

## Australian ground gravity data compilation

We have downloaded, cleaned, and combined all available
<a href="http://www.ga.gov.au/">Geoscience Australia</a>
ground gravity data (as of October 2020) into a single
<a href="https://en.wikipedia.org/wiki/NetCDF">netCDF</a> file.
The archive includes metadata following the
<a href="http://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html">CF conventions</a>
for easier loading and plotting using standard tools like
<a href="http://xarray.pydata.org/">xarray</a>.

<ul class="fa-ul">
<li>
<i class="fa-li fa fa-download"></i> Download:
<a href="https://doi.org/10.6084/m9.figshare.13643837">dataset in netCDF format</a>
</li>
<li>
<i class="fa-li fab fa-github"></i> Source code:
<a href="https://github.com/compgeolab/australia-gravity-data">compgeolab/australia-gravity-data</a>
</li>
<li>
<i class="fa-li fa fa-gavel"></i> License:
<a href="https://creativecommons.org/licenses/by/4.0/">CC-BY 4.0</a>
</li>
</ul>

<p class="text-muted">
This compilation is based on the one provided by
<a href="https://doi.org/10.26186/5c1987fa17078">Wynne (2018)</a>,
which is distributed under
<a href="https://creativecommons.org/licenses/by/4.0/">CC-BY 4.0</a>.
</p>

</div>
<div class="col-md-5 justify-content-center">

{%- set caption = "Map of the mean gravity disturbance data in 0.1° blocks for Australia." %}
<a href="https://github.com/compgeolab/australia-gravity-data">
<img src="/images/australia-ground-gravity.jpg" alt="{{ caption }}">
</a>
<p class="fs-6 text-muted text-center">
{{ caption }}
</p>

</div>
</div>


<div class="row mt-5 gy-5 gx-5">
<div class="col-md-7">

## Depth to the crust-mantle boundary of South America

<p>
Gravity data are among the most widely used means of investigating the depth to
the crust-mantle boundary (known as the Moho).
We have developed a method and software to estimate Moho depth from gravity
data in
<a href="/publications/moho-tesseroid-inversion.html">Uieda & Barbosa
(2017)</a>,
along with estimated values for South American and the adjacent oceans.
</p>

<ul class="fa-ul">
<li>
<i class="fa-li fa fa-download"></i> Download:
<a href="https://doi.org/10.6084/m9.figshare.3987267">model, data, &
source code</a>
</li>
<li>
<i class="fa-li fab fa-github"></i> Source code:
<a href="https://github.com/pinga-lab/paper-moho-inversion-tesseroids">pinga-lab/paper-moho-inversion-tesseroids</a>
</li>
<li>
<i class="fa-li fa fa-gavel"></i> License:
<a href="https://creativecommons.org/licenses/by/4.0/">CC-BY 4.0</a>
</li>
</ul>

</div>
<div class="col-md-5 order-md-first">

{%- set caption = "Maps of the depth to the crust-mantle boundary under South America (left) and differences between gravity- and seismologically-derived depths (right)." %}
<a href="/publications/moho-tesseroid-inversion.html">
<img src="/images/south-american-moho.jpg" alt="{{ caption }}">
</a>
<p class="fs-6 text-muted text-center">
{{ caption }}
</p>

</div>
</div>
