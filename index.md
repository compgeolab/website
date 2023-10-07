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
template: index.html
---

{% import "macros.html" as macros %}

## About us

The **CompGeoLab** is a research group based at the
[{{ config.location.university }}][usp].
We are experts in solving **inverse problems** in the field of **Geophysics**.
For example, determining the inner density distribution of the Earth from
measured disturbances in the Earth's gravity field.
These are the main tools used by geoscientists to **image the inside** of the
Earth and other planets.

{{ macros.figure("images/research-highlights.jpg", caption="Four examples of our research outputs. Top left: automatic detection of anomalies in magnetic microscopy data. Top right: compilation of airborne magnetic data for Antarctica. Bottom left: a tesseroid (spherical prism) discretized with our adaptive algorithm for gravity modeling. Bottom right: estimated Moho depth for South America from gravity data and the misfit with seismological estimates.", alt="Figure with four panels. Top left is a map showing red and blue blobs and black squares surrounding each one. Top right is a map of Antarctica with red and blue points overlaid covering a large portion of the continent. Bottom left is a spherical 8-sided prism on top of the globe with white lines showing how it's broken up irregularly. Bottom right are two maps of South America, one colored green to yellow representing the Moho depth, larger around the Andes and smaller in towards the Atlantic coast, the other has scattered colored dots showing larger differences in the Andes and smaller elsewhere." ) }}

We also specialize in building **open-source scientific software**.
Our team works on several tools and projects, both developing
tools in-house and contributing across the larger scientific ecosystem:

[**Fatiando a Terra**][fatiando]:
A collection of Python tools for geophysics. The Fatiando tools are the heart
of most of our research and teaching efforts. This is the main project on which
we work.

[**xlandsat**][xlandsat]:
A small Python library for loading Landsat multi-spectral remote sensing scenes
from downloaded from USGS EarthExplorer into xarray.Dataset containers. It
takes care of reading the metadata and organizing the bands into a single data
structure for easier manipulation, processing, and visualization.

[**The Generic Mapping Tools**][gmt]:
GMT is one of the most widely used and loved open-source software in the
geosciences. Our team contributes to both GMT and the PyGMT library which
brings all the power of GMT to the Scientific Python ecosystem.

[**Tesseroids**][tesseroids]:
A collection of command-line programs for modeling the gravitational potential,
acceleration, and gradient tensor. Tesseroids supports models and computation
grids in Cartesian and spherical coordinates.

[usp]: https://www.iag.usp.br/
[fatiando]: https://www.fatiando.org/
[xlandsat]:
[explorer]:
[pygmt]:
[tesseroids]:
