---
title: Data & Models
layout: page
order: date
---

Along the course of our research, we often produce open-access datasets and
models. These products are available for free under permissive licenses
(usually the
[Creative Commons Attribution](https://creativecommons.org/licenses/by/4.0/)
license). You can usually find links to all data and model products in the
publications themselves. Below is a curated list of datasets and models
generated or compiled by the group.

<div class="home-block">
<div class="row">
<div class="col-md-6">

<h2>Australian ground gravity data compilation</h2>

<p>
We have downloaded, cleaned, and combined all available
<a href="http://www.ga.gov.au/">Geoscience Australia</a>
ground gravity data (as of October 2020) into a single
<a href="https://en.wikipedia.org/wiki/NetCDF">netCDF</a> file.
The archive includes metadata following the
<a href="http://cfconventions.org/Data/cf-conventions/cf-conventions-1.8/cf-conventions.html">CF conventions</a>
for easier loading and plotting using standard tools like
<a href="http://xarray.pydata.org/">xarray</a>.
</p>

<ul class="fa-ul">
    <li>
        <i class="fa-li fa fa-download"></i> Download:
        <a href="https://github.com/compgeolab/australia-gravity-data/releases/latest">australia-ground-gravity.nc</a>
    </li>
    <li>
        <i class="fa-li fa fa-github"></i> Source code:
        <a href="https://github.com/compgeolab/australia-gravity-data">compgeolab/australia-gravity-data</a>
    </li>
    <li>
        <i class="fa-li fa fa-gavel"></i> License:
        <a href="https://creativecommons.org/licenses/by/4.0/">CC-BY 4.0</a>
    </li>
</ul>

<p class="caption">
This compilation is based on the one provided by
<a href="https://doi.org/10.26186/5c1987fa17078">Wynne (2018)</a>,
which is distributed under
<a href="https://creativecommons.org/licenses/by/4.0/">CC-BY 4.0</a>.
</p>

</div>
<div class="col-md-6">

<a href="https://github.com/compgeolab/australia-gravity-data">
<img src="/images/australia-ground-gravity.jpg" alt="Map of the mean gravity disturbance data in 0.1° blocks for the whole of Australia.">
</a>
<p class="caption">
Map of the mean gravity disturbance data in 0.1° blocks for Australia.
</p>

</div>
</div>
</div>


<div class="home-block">
<div class="row">
<div class="col-md-6">

<h2>Depth to the crust-mantle boundary of South America</h2>

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
        <i class="fa-li fa fa-github"></i> Source code:
        <a href="https://github.com/pinga-lab/paper-moho-inversion-tesseroids">pinga-lab/paper-moho-inversion-tesseroids</a>
    </li>
    <li>
        <i class="fa-li fa fa-gavel"></i> License:
        <a href="https://creativecommons.org/licenses/by/4.0/">CC-BY 4.0</a>
    </li>
</ul>

</div>
<div class="col-md-6">

<a href="https://github.com/pinga-lab/paper-moho-inversion-tesseroids">
<img src="/images/south-american-moho.jpg" alt="Maps of the Moho depth for South America (left) and differences between gravity- and seismologically-derived depths (right).">
</a>
<p class="caption">
Maps of the Moho depth for South America (left) and differences between
gravity- and seismologically-derived depths (right).
</p>

</div>
</div>
</div>
