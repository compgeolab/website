---
title: Our research
template: base.html
---

{% import "macros.html" as macros %}

# {{ page.title }}

<div class="lead">

We focus our efforts on creating and applying new methods for **3D modeling and
data processing**, mostly for gravimetry and magnetometry.

</div>


## Magnetic microscopy

The magnetization locked in minerals at the time of their formation is a
gateway to the **Earth's distant past**.
So far, researchers have only been able to make bulk measurements from each
sample.
Magnetic microscopy technology is now allowing us to distinguish **the magnetic
fields of the individual minerals** that make up the rock sample.
Our group is working with experts in paleomagnetism to **develop new methods**
that are capable of unlocking the huge potential of these new data.

{{ macros.figure(src="../images/magnetic-microscopy-example-data.jpg", alt="Red and blue map showing dipolar anomalies at a scale of 20 micrometers.", caption="Example magnetic microscopy data showing tiny magnetic anomalies on the order of 20µm in size.") }}

<div class="callout">

Our work on this theme:

* [Full vector inversion of magnetic microscopy images using Euler deconvolution as a priori information](https://github.com/compgeolab/micromag-euler-dipole)

</div>


## Antarctic geothermal heat flow

Heat flow from the Earth's interior is an important parameter for how **ice
sheets flow** and how the Earth's crust rebounds upwards once ice mass is
displaced, influencing **sea-level rise**.
Magnetic anomaly data is one of the few ways we have to determine heat flow.
Our group is working to improve the way **airborne and satellite magnetic
data** are merged and modelled to produce heat flow estimates.

{{ macros.figure(src="../images/antarctica-magnetic-data.jpg", alt="Map of Antarctica overlaid by red, white, and blue points representing magnetic measurements. The data coverage has a lot of gaps.", caption='The <a href="https://doi.org/10.1029/2018GL078153">ADMAP2</a> compilation of open-access airborne magnetic anomaly data for Antarctica.') }}

<div class="callout">

Our work on this theme:

* {{ macros.page_link("news/pgr-conference2023", page, site) }}

</div>


## Machine learning & data processing

It's undeniable that a **machine learning** frenzy has taken over the world.
Geoscientists have been doing similar things for decades, for example the
**equivalent sources technique** in gravity and magnetics is basically a
supervised-learning method. Given the many similarities, we are applying and
adapting machine learning techniques and best-practices to geophysical
problems.

{{ macros.figure(src="../images/block-mean-example.jpg", alt="3 maps of California with colored points representing different types of uncertainty calculations with each being slightly different from the observed data uncertainties.", caption="Spatial data has uncertainties which need to be handled properly. There are different ways to use uncertainties as data weights for processing.") }}

<div class="callout">

Our work on this theme:

* [Gradient-boosted equivalent sources](https://github.com/compgeolab/eql-gradient-boosted) ([video abstract](https://doi.org/10.6084/m9.figshare.14515188))
* [Verde: Processing and gridding spatial data using Green's functions](https://doi.org/10.21105/joss.00957) ([project documentation](https://www.fatiando.org/verde/latest/))
* [Evaluating the accuracy of equivalent-source predictions using cross-validation](https://doi.org/10.6084/m9.figshare.12245372)

</div>


## Geophysical inversion and imaging

Our ultimate goal as geophysicists is to **understand the inner structure and
dynamics of the Earth** from surface observations. This is a tough mathematical
and computational problem: an ill-posed **inverse problem**, to which a
solution might not exist or be non-unique and unstable.
We develop methods to overcome these challenges and solve different kinds of
inverse problems that arise in geophysics.

{{ macros.figure(src="../images/quadrilatero-ferrifero-density-model.png", alt="3D rendering of white blocks with topography and some red blocks spread in a thin vain representing the estimated iron ore body.", caption="Modelled density anomalies associated with iron-ore formations derived from observed gravity disturbances.") }}

<div class="callout">

Our work on this theme:

* [Fast non-linear gravity inversion in spherical coordinates with application to the South American Moho](https://github.com/pinga-lab/paper-moho-inversion-tesseroids)
* [Robust 3D gravity gradient inversion by planting anomalous densities](https://github.com/pinga-lab/paper-planting-densities)

</div>


## Forward modeling

A key component for solving an inverse problem is first solve the **forward
problem** (predicting observed data from a known model of the subsurface).
One of our main research themes is the development methods for
forward modeling **gravitational fields** caused by a tesseroid (a segment of a
sphere).
This is a surprisingly difficult task but is crucial to model geology at
continental and global scales.

{{ macros.figure(src="../images/tesseroid.jpg", alt="Drawing of a curved prism sitting on top of a curved Earth. The prism is cut by white lines that represent the discretization.", caption="A tesseroid (spherical prism) discretized using our adaptive algorithm.") }}

<div class="callout">

Our work on this theme:

* [Gravitational field calculation in spherical coordinates using variable densities in depth](https://github.com/pinga-lab/tesseroid-variable-density)
* [Tesseroids: forward modeling gravitational fields in spherical coordinates](https://github.com/pinga-lab/paper-tesseroids)

</div>
