---
title: Research
layout: page
order: date
banner: disturbance.jpg
banner_description: "Map of the gravity disturbance around the Pacific Ocean."
---

{% from "utils.html" import make_index, make_tags, make_tag, fa %}

My main topic of research is the development of methods to solve
[inverse problems in geophysics](https://en.wikipedia.org/wiki/Inverse_problem).
For example, estimating
[density anomalies in the subsurface from measured disturbances in gravity][/publications/planting-inversion].
Central to all of my projects is the open-source software upon which I
implement the new methods.

I have an **open by default** policy for my research and teaching output.
Pretty much everything I do is freely available online, usually on
[Github](https://github.com/leouieda/).

# Research Themes

## Inverse problems

As a geophysicist, my ultimate goal is to infer the physical properties of the
inner Earth and its processes from surface observations.
This is an ill-posed inverse problem, to which a solution might not exist or be
non-unique and unstable.
I develop methods for solving different kinds of inverse problems using
several sets of constraints to overcome the instability of the solution.

<div class="research-index">
    {{ make_tags(["inversion", "gravity", "magnetic", "euler-deconvolution"], icon=true) }}
    {{ make_index(site.reflinks["/tag/inversion"].content[:4], site, hr=false, date=false) }}
</div>


## Forward modeling

A key component for solving an inverse problem is first solve the "forward
problem".
This is jargon for predicting data given a set of model parameters.
One of the first research problems on which I worked was developing a method
for forward modeling gravitational fields caused by
[a tesseroid](https://doi.org/10.6084/m9.figshare.1495521) (a spherical prism).
I'm still doing work related to this theme.

<div class="research-index">
    {{ make_tags(["forward-modeling", "tesseroids"], icon=true) }}
    {{ make_index(site.reflinks["/tag/forward-modeling"].content[:4], site, hr=false, date=false) }}
</div>


## Data processing

There is no turning back from the machine learning frenzy that has taken over
the world.
Geoscientists have been doing similar things for decades but with different
names and objectives.
One of these things is called the
"equivalent layer technique"
in gravity and magnetics.
Similar methods in different fields have many different names, for example
[radial basis functions](https://en.wikipedia.org/wiki/Radial_basis_function)
or [Green's functions interpolation](https://doi.org/10.1002/2016GL070340).
All of these methods are linear regressions in which we fit a linear model to
some data and then use the model to predict new data.
The difference with standard machine learning is that the linear model we use
has physical meaning.
For gravity data, the model is the gravitational attraction of point sources,
whereas for GPS data, the model is the elastic deformation of medium.
Given the many similarities, I have been very interested in applying other
machine learning techniques, like model selection, to these geophysical
problems.

<div class="research-index">
    {{ make_tags(["equivalent-layer"], icon=true) }}
    {{ make_index(site.reflinks["/tag/equivalent-layer"].content[:4], site, hr=false, date=false) }}
</div>
