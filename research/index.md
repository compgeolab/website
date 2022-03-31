---
title: Our research themes
template: base.html
---

{% from "macros.html" import figure, video %}

# {{ page.title }}

<p class="lead">
We focus on the creation and application of new methods for geophysical
<strong>modeling and data processing</strong>, mostly in the fields of
gravimetry and magnetometry.
</p>

<div class="row mt-5 gy-5 gx-5">
<div class="col-md-7">

## Inverse problems

Our ultimate goal as geophysicists is to **understand the inner structure and
dynamics of the Earth** from surface observations. This is a tough mathematical
and computational problem: an ill-posed **inverse problem**, to which a
solution might not exist or be non-unique and unstable.
We develop methods to overcome these challenges and solve different kinds of
inverse problems that arise in geophysics.

</div>
<div class="col-md-5">

{{ video(src="../images/planting-inversion.mp4", caption="The planting method for solving the inverse problem of estimating density from observed gravity disturbances.", style="display: block; margin: 0 auto; width: 70%;") }}

</div>
</div>

<div class="row mt-5 gy-5 gx-5">
<div class="col-md-7">

## Forward modeling

A key component for solving an inverse problem is first solve the **forward
problem** (predicting observed data from a known model of the subsurface).
One of our main research themes is the development methods for
forward modeling **gravitational fields** caused by a tesseroid (a segment of a
sphere).
This is a surprisingly difficult task but is crucial to model geology at
continental and global scales.

</div>
<div class="col-md-5 order-md-first">

{{ figure(src="../images/tesseroid.jpg", caption="A tesseroid (spherical prism) discretized using our adaptive algorithm.") }}

</div>
</div>

<div class="row mt-5 gy-5 gx-5">
<div class="col-md-7">

## Data processing

There is no turning back from the **machine learning** frenzy that has taken
over the world. Geoscientists have been doing similar things for decades, for
example the **equivalent layer technique** in gravity and magnetics. Given the
many similarities, we are applying other machine learning techniques to these
geophysical problems.

</div>
<div class="col-md-5">

{{ figure(src="../images/block-mean-example.jpg", caption="Spatial data has uncertainties which need to be handled properly. There are different ways to use uncertainties as data weights for processing.") }}

</div>
</div>
