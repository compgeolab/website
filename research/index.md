---
title: Our research themes
template: base.html
---

{% from "macros.html" import figure, video %}

# {{ page.title }}

<p class="lead mb-5">
We focus on the creation and application of new methods for geophysical
<strong>modeling and data processing</strong>, mostly in the fields of
gravimetry and magnetometry.
</p>


## Machine learning & data processing

<div class="row mb-5 gy-5 gx-5">
<div class="col-md-7">

It's undeniable that a **machine learning** frenzy has taken over the world.
Geoscientists have been doing similar things for decades, for example the
**equivalent layer technique** in gravity and magnetics. Given the many
similarities, we are applying other machine learning techniques to these
geophysical problems.

<button class="btn btn-primary me-1 mb-2" type="button"
    data-bs-toggle="collapse" data-bs-target="#collapse-abstract-ml"
    aria-expanded="false" aria-controls="collapse-abstract-ml">
  Our work on this theme <i class="fa fa-chevron-circle-down ms-1" aria-hidden="true"></i>
</button>
<div id="collapse-abstract-ml" class="collapse paper-info mt-2 overflow-hidden">

Selected publications:

* [Gradient-boosted equivalent sources (Soler & Uieda, 2021)](https://github.com/compgeolab/eql-gradient-boosted)
* [Verde: Processing and gridding spatial data using Green's functions (Uieda, 2018)](https://doi.org/10.21105/joss.00957)

</div>

</div>
<div class="col-md-5">

{{ figure(src="../images/block-mean-example.jpg", caption="Spatial data has uncertainties which need to be handled properly. There are different ways to use uncertainties as data weights for processing.") }}

</div>
</div>

## Geophysical inversion and imaging

<div class="row mb-5 gy-5 gx-5">
<div class="col-md-7">

Our ultimate goal as geophysicists is to **understand the inner structure and
dynamics of the Earth** from surface observations. This is a tough mathematical
and computational problem: an ill-posed **inverse problem**, to which a
solution might not exist or be non-unique and unstable.
We develop methods to overcome these challenges and solve different kinds of
inverse problems that arise in geophysics.

<button class="btn btn-primary me-1 mb-2" type="button"
    data-bs-toggle="collapse" data-bs-target="#collapse-abstract-inv"
    aria-expanded="false" aria-controls="collapse-abstract-inv">
  Our work on this theme <i class="fa fa-chevron-circle-down ms-1" aria-hidden="true"></i>
</button>
<div id="collapse-abstract-inv" class="collapse paper-info mt-2 overflow-hidden">

Selected publications:

* [Fast non-linear gravity inversion in spherical coordinates with application to the South American Moho (Uieda & Barbosa, 2017)](https://github.com/pinga-lab/paper-moho-inversion-tesseroids)
* [Robust 3D gravity gradient inversion by planting anomalous densities (Uieda & Barbosa, 2012)](https://github.com/pinga-lab/paper-planting-densities)

</div>

</div>
<div class="col-md-5">

{{ video(src="../images/planting-inversion.mp4", caption="The planting method for solving the inverse problem of estimating density from observed gravity disturbances.", style="display: block; margin: 0 auto; width: 70%;") }}

</div>
</div>

## Forward modeling

<div class="row gy-5 gx-5">
<div class="col-md-7">

A key component for solving an inverse problem is first solve the **forward
problem** (predicting observed data from a known model of the subsurface).
One of our main research themes is the development methods for
forward modeling **gravitational fields** caused by a tesseroid (a segment of a
sphere).
This is a surprisingly difficult task but is crucial to model geology at
continental and global scales.

<button class="btn btn-primary me-1 mb-2" type="button"
    data-bs-toggle="collapse" data-bs-target="#collapse-abstract-fwd"
    aria-expanded="false" aria-controls="collapse-abstract-fwd">
  Our work on this theme <i class="fa fa-chevron-circle-down ms-1" aria-hidden="true"></i>
</button>
<div id="collapse-abstract-fwd" class="collapse paper-info mt-2 overflow-hidden">

Selected publications:

* [Gravitational field calculation in spherical coordinates using variable densities in depth (Soler et al., 2019)](https://github.com/pinga-lab/tesseroid-variable-density)
* [Tesseroids: forward modeling gravitational fields in spherical coordinates (Uieda et al., 2016)](https://github.com/pinga-lab/paper-tesseroids)

</div>

</div>
<div class="col-md-5">

{{ figure(src="../images/tesseroid.jpg", caption="A tesseroid (spherical prism) discretized using our adaptive algorithm.") }}

</div>
</div>
