---
title: "New paper proposing a new cost-effective way to automatically analyze magnetic microscopy images"
date: 2024-08-07
---

{% import "macros.html" as macros %}

After over 1 year in review (😮‍💨), we have a new open-access paper by
lab member [Gelson F. Souza Junior](../team#Souza-junior), the first of his PhD
🎉 :

> Souza‐Junior, G. F., Uieda, L., Trindade, R. I. F., Carmo, J., & Fu, R.
> (2024). Full vector inversion of magnetic microscopy images using Euler
> deconvolution as prior information. Geochemistry, Geophysics, Geosystems, 25,
> e2023GC011082. doi:[10.1029/2023GC011082](https://doi.org/10.1029/2023GC011082)

## About

In short, very small magnetic particles in rocks and other materials can store
information about what the Earth’s magnetic field was like in the past.
But not all particles are good recorders of this magnetic information, and some
may have recorded different overlapping directions and strengths.
So it is important to measure each particle separately in order to identify and
separate the good recorders from the bad ones.
A device called a "quantum diamond microscope" is able to measure the
magnetic field near the surface of a rock sample at microscopic scale.
We propose a new method for processing data from this microscope that is able
to find out the individual magnetizations of large amounts of small magnetic
particles automatically.
We created a computer program to execute the method, which calculates the 3D
position and magnetization of each particle using the simple model of a
magnetic dipole.
We tested the method on simulated data, using fake magnetic particles for which
we know the correct magnetization and position, and real data, both of which
showed good results in most cases.
The method we created has the potential to enable the widespread study of the
magnetism of natural materials with more detail than before.

Here is an example of what the data and results we can obtain from it look
like:

{{ macros.figure(src="../images/news/micromag-euler-dipole-paper-figure.jpg", alt="Two figures side by side. On the right, a stereogram with dots showing estimated dipole moment directions with some dots concentrate in upper part, a few scattered points, and most dots concentrated in the bottom. On the left, a gray-scale map with some dipolar signals overlaid by colored vectors of various sizes, most pointing up or down.", caption="Results of applying the method we propose in the paper to a <a href='https://doi.org/10.6084/M9.FIGSHARE.22965200.V1'>real magnetic microscopy image of a speleothem sample</a>. The sample contains magnetite and hematite and was magnetized first with strong field in the +y direction and then with a weak field in the -y direction. This results is magnetites aligned with -y and hematites aligned with +y. Our estimated directions fit this expectation and allow us to map the occurrence of both minerals in the same. Modified from a figure in the paper.") }}

The main advantage of the method we came up with is that it can yield results
for even small magnetic particles requiring only the data itself and a few
seconds of processing times.
Other techniques available usually required either manual picking of the
signals in the images or expensive and time-consuming tomography data.

## Open science

All of our results and the figures in the paper can be reproduced with the
material in the GitHub repository
[compgeolab/micromag-euler-dipole](https://github.com/compgeolab/micromag-euler-dipole).
It contains a [`REPRODUCING.md`](https://github.com/compgeolab/micromag-euler-dipole/blob/main/REPRODUCING.md)
file with instructions for setting up your computing environment and running
the code.
The repository is also [archived on figshare](https://doi.org/10.6084/m9.figshare.22672978)
for long term availability and to provide a citation point.

The method is being implemented by MSc student
[Yago Moreira Castro](../team#YagoMCastro) into the open-source software project
[Magali](https://github.com/fatiando/magali), which is a part of
[Fatiando a Terra](https://www.fatiando.org/).
Yago is also working with Gelson to make improvements to the method and
implementing other quality-of-life features, such as plotting support and
statistics of vectors and directions.

![Magali logo (a watermelon cut in half with dipoles as seeds)](https://raw.githubusercontent.com/fatiando/magali/5e260e734ebf6b7e73af681c86d4589b9a2ed10b/doc/_static/readme-banner.png)

## History

The idea for this paper came from a chat I had with
[Prof. Ricardo Trindade](../team#ricardo) at AGU 2019, where he presented the
problem and I realised it was very similar to
things I had worked on before
in the [PINGA lab](https://www.pinga-lab.org)
([Melo et al. (2013)](https://doi.org/10.1190/geo2012-0515.1)
and [Oliveira Jr. et al. (2015)](https://doi.org/10.5194/npg-22-215-2015)).
We started planning a collaboration to combine the CompGeoLab's expertise in applied
geophysics and [USPMag](https://paleomagnetismo.iag.usp.br)'s long track record
in paleomagnetism.

The manuscript was originally published [as a preprint n June 2023]({{
macros.pretty_relative_link(site["news/preprint-micromag-euler-dipole"], page)
}}) and took much to long in the peer-review process.
But we're very happy that it's finally out because Gelson is already
[working on many improvements to the method]({{
macros.pretty_relative_link(site["news/castlemeeting2024"], page)
}})!

Leo

> This research is being developed under our [Royal Society grant](rsoc-mag-microscopy-2022.html) and Gelson's PhD, which is funded by [FAPESP](https://fapesp.br/).

> The plain language description of the paper was originally published in the
> paper and preprint, both licensed CC-BY.
