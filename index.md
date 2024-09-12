---
custom_page_title: Computer-Oriented Geoscience Lab
banner_image: images/banner.jpg
banner_title: Geophysical research powered by open-source software
banner_subtitle: |
  At the <strong>Computer-Oriented Geoscience Lab</strong>, we design
  state-of-the-art computational tools for the Geosciences.
  <strong>Source code included.</strong>
banner_links:
  - name: Meet the team
    id: team/index
  - name: Our research
    id: research/index
  - name: Lab manual
    id: manual/index
  - name: <i class="fab fa-github" aria-label="hidden"></i> GitHub
    id: https://github.com/compgeolab
template: home.html
---

{% import "macros.html" as macros %}

## About us

The **CompGeoLab** is a
[research group]({{ macros.pretty_relative_link(site["team/index"], page) }})
based at the
[{{ config.location.university }}][usp], Brazil.
We are experts in solving **inverse problems** in the field of **Geophysics**,
particularly in **gravity and magnetic methods** (AKA potential-field methods).
Inverse problems are the means by which geoscientists **image the inside** of
the Earth and other planets.
For example, we are able to determine the inner density distribution of the
Earth from measured disturbances in the Earth's gravity field.
We are also champions of **open science** and **reproducible research**.
All of our teaching and research efforts are symbiotic with the development of
**open source software** for geoscience.

{{ macros.figure("images/research-highlights.jpg", caption="Example research outputs. <strong>Top left:</strong> automatic detection of anomalies in magnetic microscopy data. <strong>Top right:</strong> compilation of airborne magnetic data for Antarctica. <strong>Bottom left:</strong> a tesseroid (spherical prism) discretized with our adaptive algorithm for gravity modeling. <strong>Bottom right:</strong> estimated Moho depth for South America from gravity data (left) and the misfit with seismological estimates (right).", alt="Figure with four panels. Top left is a map showing red and blue blobs and black squares surrounding each one. Top right is a map of Antarctica with red and blue points overlaid covering a large portion of the continent. Bottom left is a spherical 8-sided prism on top of the globe with white lines showing how it's broken up irregularly. Bottom right are two maps of South America, one colored green to yellow representing the Moho depth, larger around the Andes and smaller in towards the Atlantic coast, the other has scattered colored dots showing larger differences in the Andes and smaller elsewhere." ) }}


## Open source

Our team works on several tools and projects, both developed in-house and
across the larger scientific ecosystem:

* [**Fatiando a Terra**][fatiando]: A collection of Python tools for
  geophysics. The Fatiando tools are the heart of most of our research and
  teaching efforts. This is the main project on which we work.
* [**xlandsat**][xlandsat]: A small Python library for loading and analyzing
  Landsat scenes downloaded from [USGS EarthExplorer][explorer] with the power
  of xarray into [xarray][xarray].
* [**The Generic Mapping Tools**][gmt]: One of the most widely used and loved
  open-source software in the geosciences. Our team contributes to both GMT and
  the [PyGMT][pygmt] library which brings all the power of GMT to the
  Python stack.
* [**Tesseroids**][tesseroids]: A collection of command-line programs for
  modeling the gravitational potential, acceleration, and gradient tensor.
  Tesseroids supports models and computation grids in Cartesian and spherical
  coordinates.

We also **publish all of the code and data** needed to reproduce our projects
on [our <i class="fab fa-github" aria-hidden="true"></i> GitHub organization][github].

[usp]: https://www.iag.usp.br/
[fatiando]: https://www.fatiando.org/
[xlandsat]: https://www.compgeolab.org/xlandsat
[explorer]: https://earthexplorer.usgs.gov/
[xarray]: https://xarray.dev/
[gmt]: https://www.generic-mapping-tools.org/
[pygmt]: https://www.pygmt.org
[tesseroids]: https://tesseroids.leouieda.com/
[github]: https://github.com/compgeolab
