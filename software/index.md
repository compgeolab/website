---
title: Software
layout: page
order: date
banner: disturbance.jpg
banner_description: "Map of the gravity disturbance around the Pacific Ocean."
---

{% from "utils.html" import make_index, make_tags, make_tag, fa %}

Programming is a requirement for method development.
By definition, there is no existing software that implements your new method.
I program mostly in [Python](https://www.python.org/) but I'm also proficient
in [C](https://en.wikipedia.org/wiki/C_(programming_language)).
All of our software contributions are
[open-source](https://en.wikipedia.org/wiki/Open-source_software)
and hosted on [Github](https://github.com/leouieda/).

<div class="research-index">
    {{ make_tags(["open-source"], icon=true) }}
</div>

I'm the creator and/or maintainer of the following projects:


## Fatiando a Terra ([www.fatiando.org](https://www.fatiando.org))

Fatiando is a Python library for modeling and inversion in geophysics.
The name is Portuguese for "*slicing the Earth*" (like a loaf of bread).
I started development of Fatiando in 2010 while working on my
[Masters degree](https://www.leouieda.com/about/masters.html).
I now use it regularly for my research and also for much of my teaching
material.
Most recent papers published by the [PINGA lab](http://www.pinga-lab.org) use
it in some way.
Fatiando was featured in the
[89th Boletim SBGf (PDF in Portuguese)](/pdf/boletim-sbgf-fatiando-89-2014.pdf).

In 2018, I started work to [convert Fatiando into several independent
packages](https://www.leouieda.com/blog/future-of-fatiando.html):

* [Verde](https://www.fatiando.org/verde/): The first one I started working on. A
  library for gridding and spatial data processing.
* [Pooch](https://www.fatiando.org/pooch/): A small Python library that manages the
  download and caching of sample data sets. It will be used in support of the other
  packages.
* [RockHound](https://www.fatiando.org/rockhound/): Download common geophysical models
  and datasets (think PREM, CRUST1.0, ETOPO1) and load them into Python data structures.
* [Harmonica](https://www.fatiando.org/harmonica/dev/): Library for processing and
  modeling gravity and magnetic data.

## Tesseroids  ([www.tesseroids.org](http://www.tesseroids.org))

Command-line programs for gravity forward modeling. This was my first software
project. I started working on *Tesseroids* in 2008 for my [Bachelor's thesis
project](https://www.leouieda.com/about/bachelors.html) and continued in collaboration with Professor [Carla
Braitenberg](https://www2.units.it/braitenberg/) from the [University of
Trieste](https://dmg.units.it/). The paper "[/publications/tesseroids]"
describes the algorithms behind [version
1.2.0](https://doi.org/10.5281/zenodo.16033) of the software, which ended up
becoming a chapter of my [PhD thesis](https://www.leouieda.com/about/phd.html).

## PyGMT ([www.pygmt.org](https://www.pygmt.org))

A modern Python interface for the [Generic Mapping Tools](http://gmt.soest.hawaii.edu/).
I started building PyGMT (formerly GMT/Python) in 2017 as part of my
[postdoc at the University of Hawaii](https://www.leouieda.com/blog/hawaii-gmt-postdoc.html) with
[Paul Wessel](http://www.soest.hawaii.edu/wessel) (the co-creator and main developer of
GMT).
Work is still in early stages but there is a minimum working example on the
website. PyGMT was used to generate the bathymetry and topography banner
images for this website.
