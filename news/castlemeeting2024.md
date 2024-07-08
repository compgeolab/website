---
title: "Talk on improved magnetic microscopy inversion at the 2024 Castle Meeting"
date: 2024-07-08
---


{% import "macros.html" as macros %}

Last Thursday, lab member [Gelson F. Souza Junior](../team#Souza-junior) gave a
talk at the [2024 Castle Meeting](https://castlemeeting.org/) at  Utrecht, The
Netherlands.
The talk showed the first results of a significant improvement that we made to
our [magnetic microscopy inversion method]({{
macros.pretty_relative_link(site["news/preprint-micromag-euler-dipole"], page)
}}).
We are now able to correctly recover the dipole moments of most sources in an
image, even the ones subject to large interference from other sources!

{{ macros.figure(src="../images/news/castlemeeting2024.jpg", alt="Presenter (brown-skinned male in a green t-shirt) behind lectern next to presentation screen with introduction slide. Slide contains classic paleomagnetic studies that use samples of approximated 10 cm³ with hundreds of thousands to millions of individual magnetic particles. Also seen are the backs of the heads of 8 audience members.", caption="Gelson presenting the motivation to our studies into magnetic microscopy inversion to a captive audience.") }}

This research is being developed under our [Royal Society
grant](rsoc-mag-microscopy-2022.html) and Gelson's PhD, which is funded by
[FAPESP](https://fapesp.br/).

## Abstract

Paleomagnetic data are typically obtained from bulk samples, where the signal
results from the combined magnetic moments of hundreds of thousands to millions
of magnetic particles within the sample volume, including both stable and
unstable remanence carriers. Recently, magnetic microscopy techniques have
enabled the investigation of individual grains by directly imaging their
magnetic fields. However, determining the magnetic moments of individual grains
is challenging because of the intrinsic ambiguity in the inversion of potential
field data and the large number of grains in any microscopy image. Recently, we
proposed a window-based technique capable of estimating the magnetization of
each magnetic source using only magnetic microscopy data by applying the Euler
deconvolution as prior information of the source position. Upon further
investigation of inversions using magnetic microscopy data, we encountered
situations in which the outcomes of this methodology were not adequate,
particularly when particles are clustered together or when the signal of a
smaller particle is embedded in the signal of a larger one. Although the
algorithm removed the unreliable estimates in the final filtering process, it
would be desirable to estimate the positions and dipole moments of these
sources correctly. This led to the development of a more robust and accurate
approach to account for the mutual interference between the sources and also
for the undesirable static shifts in the magnetic field during the
measurements. The revised method incorporates an iterative Euler deconvolution
scheme and non-linear optimization techniques to refine position and magnetic
moment estimates from the linear inversion. Our synthetic data application
demonstrated significant improvements in accuracy compared to the standard
method, particularly in scenarios with high levels of source interaction. The
real data application further validated the method, showing better clustering
of magnetization directions and less penalization of weaker sources. The
proposed approach enhances the precision of inversion analyses, providing a
substantial advancement in magnetic microscopy. It effectively mitigates the
impact of stronger sources and static shifts, ensuring more accurate and
reliable results in studying paleomagnetic and rock magnetic properties.
