---
title: Our research
template: base.html
---

{% import "macros.html" as macros %}

<div class="lead">

We focus our efforts on creating and applying new methods for **3D modeling and
data processing**, mostly for gravimetry and magnetometry. Below, you'll find
the main research themes that we pursue.

</div>


<section class="extra-space flow">

## Magnetic microscopy

The magnetization that gets locked in some minerals (known as [*ferromagnetic minerals*](https://en.wikipedia.org/wiki/Ferromagnetism)) at the time of their formation is one of a few gateways we have into the **Earth's distant past**.
So far, researchers have mostly only been able to make bulk measurements of magnetization from collected rock samples.
Emerging *magnetic microscopy* technology is now allowing us to image thin-sections and distinguish **the magnetic fields of the individual minerals** that make up the rock sample.

Our group is collaborating with experts in paleomagnetism to **develop new methods and software for data processing and interpretation**, unlocking the huge potential of these exciting new datasets.

{{ macros.figure(src="../images/magnetic-microscopy-example-data.jpg", alt="Red and blue map showing dipolar anomalies at a scale of 20 micrometers.", caption='Example magnetic microscopy dataset from a thin-section of a <a href="https://en.wikipedia.org/wiki/Speleothem">speleothem</a> showing tiny magnetic anomalies (on the order of 20 µm in size) that are associated with the ferromagnetic minerals found in the rock.') }}

<div class="callout">

Our work on this theme:

* [Full vector inversion of magnetic microscopy images using Euler deconvolution as a priori information](https://github.com/compgeolab/micromag-euler-dipole)

</div>

</section>
<section class="extra-space-xl flow">

## Antarctic magnetic data and geothermal heat flow

Antarctica is a vast and poorly explored continent that is suffering greatly from the impacts of human-induced climate change.
One parameter that is crucial to understanding how Antarctica's **ice sheets will respond to climate change** is the **flow of heat coming from the Earth's crust**.
This so-called *geothermal heat flow* is needed to constrain models of how ice sheets flow and how the Earth's crust rebounds upwards once ice mass is displaced, influencing **sea-level rise**.
One of the few ways we have to determine heat flow over the entire continent is through indirect geophysical observations, like **magnetic anomaly data**.

We are working hard on improving the way that **airborne and satellite magnetic data** are processed and merged, aiming to reach the highest resolution possible from the data.
Our group is also tackling the challenging **inverse problem of producing heat flow estimates** from the magnetic data.

{{ macros.figure(src="../images/antarctica-magnetic-data.jpg", alt="Map of Antarctica overlaid by red, white, and blue points representing magnetic measurements. The data coverage has a lot of gaps.", caption='The <a href="https://doi.org/10.1029/2018GL078153">ADMAP2</a> compilation of open-access airborne magnetic anomaly data for Antarctica. We are improving the compilation by adding more recent surveys and standardizing the data, as well as developing a new process for merging these data with satellite observations.') }}

<div class="callout">

Our work on this theme:

* {{ macros.page_link("news/pgr-conference2023", page, site) }}

</div>

</section>
<section class="extra-space-xl flow">

## Geophysical data processing and interpolation

It's undeniable that a **machine learning** frenzy has taken over the world.
Geoscientists have been doing similar things for decades, for example the **equivalent sources technique** in gravity and magnetics and **spline interpolation** are basically supervised-learning methods.
Given the many similarities, it makes sense to apply and adapt machine learning techniques and best-practices to these geophysical problems.

At the lab, we are employing machine-learning methods like **ensemble techniques** and **cross-validation** to overcome key computational challenges in equivalent-source methods and data interpolation (AKA gridding).

{{ macros.figure(src="../images/gradient-boosted-equivalent-sources-gravity.jpg", alt="Two maps side by side of the area, with coastlines visible on the upper part, the left map showing red-white-blue dots scattered throughout the continental part, the right map showing a continuous red-white-blue distribution of colors.", caption='Results from our interpolation of millions of <a href="https://github.com/compgeolab/australia-gravity-data">ground gravity data from Australia</a> to a uniform height using gradient-boosted equivalent sources. <strong>Left:</strong> Section of the ground measurements of gravity disturbance (red means positive and blue means negative) from several surveys with different spacings and distributions. <strong>Right:</strong> Same section of the interpolated grid at a uniform height, which is able to retain the high resolution of the denser surveys while filling in the gaps in the data.') }}

<div class="callout">

Our work on this theme:

* [Gradient-boosted equivalent sources](https://github.com/compgeolab/eql-gradient-boosted) ([video abstract](https://doi.org/10.6084/m9.figshare.14515188))
* [Verde: Processing and gridding spatial data using Green's functions](https://doi.org/10.21105/joss.00957) ([project documentation](https://www.fatiando.org/verde/latest/))
* [Evaluating the accuracy of equivalent-source predictions using cross-validation](https://doi.org/10.6084/m9.figshare.12245372)

</div>

</section>
<section class="extra-space-xl flow">

## 3D geophysical inverse problems

Our ultimate goal as geophysicists is to **understand the inner structure and dynamics of the Earth** from surface observations.
This is a tough mathematical and computational problem: it's an ill-posed **inverse problem**, to which a solution might not exist, not be unique, and not be stable.

We develop methods to overcome these challenges and solve different kinds of inverse problems that arise in geophysics.

{{ macros.figure(src="../images/quadrilatero-ferrifero-density-model.jpg", alt="3D rendering of white blocks with topography and some red blocks spread in a thin vain representing the estimated iron ore body.", caption="Modeled density anomalies associated with iron-ore formations derived from observed gravity disturbances.") }}

<div class="callout">

Our work on this theme:

* [Euler inversion: Locating sources of potential-field data through inversion of Euler’s homogeneity equation](https://github.com/compgeolab/euler-inversion)
* [Fast non-linear gravity inversion in spherical coordinates with application to the South American Moho](https://github.com/pinga-lab/paper-moho-inversion-tesseroids)
* [Robust 3D gravity gradient inversion by planting anomalous densities](https://github.com/pinga-lab/paper-planting-densities)

</div>

</section>
<section class="extra-space-xl flow">


## Forward modeling gravity and magnetic data

A key component for solving an inverse problem is first solve the **forward problem** (predicting observed data from a known model of the subsurface).
This is often a challenging problem to solve, both mathematically and computationally.
Having a forward model that is both **accurate and performant** is the key to a reliable solution to an inverse problem.

One of our earliest research themes is the development of methods and software for modeling **gravitational fields** caused by a tesseroid (a segment of a sphere).
This is a surprisingly difficult task but is crucial to model geology at continental and global scales.
We also produce software that can model different geometries, like points, spheres, prisms, polygons, etc.

{{ macros.figure(src="../images/tesseroid.jpg", alt="Drawing of a curved prism sitting on top of a curved Earth. The prism is cut by white lines that represent the discretization.", caption="A tesseroid (spherical prism) discretized using our adaptive algorithm.") }}

<div class="callout">

Our work on this theme:

* [Gravitational field calculation in spherical coordinates using variable densities in depth](https://github.com/pinga-lab/tesseroid-variable-density)
* [Tesseroids: forward modeling gravitational fields in spherical coordinates](https://github.com/pinga-lab/paper-tesseroids)

</div>

</section>
