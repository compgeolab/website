---
title: "Gradient-boosted equivalent sources"
date: 2021-01-25
author: santisoler, uieda
repository: compgeolab/eql-gradient-boosted
preprint_server: EarthArXiv
preprint: 10.31223/X58G7C
supplement: 10.6084/m9.figshare.13604360
citation: "Soler, S., & Uieda, L. (2021). Gradient-boosted equivalent sources. EarthArXiv. doi:10.31223/x58g7c"
alm: true
layout: publication
tags: data-processing, gravity, open-source
---

# About

This paper describes how we used the gradient-boosting machine learning method
to scale equivalent source processing to millions gravity and magnetic data.
Equivalent sources allow us take into account the observation height and the
physics of potential fields (manly, they are harmonic functions) when
processing and interpolation, which are often ignored by other methods.
This leads to great results but it's involves large linear models, so
processing datasets of this magnitude is tricky.
By using gradient-boosting to fit the model in small chunks, we can process
millions of data even on a modest laptop (and in a reasonable amount of time).

This research was done entirely with [open-source software][/software] and
[open data][/data]! This means that anyone should be able to fully reproduce
our results using the information in the paper and the material in the
associated GitHub repository.

This is the final part of [Santiago's][/people/santisoler] PhD thesis.

![Visual abstract for the paper: How can we interpolate over 1 million
gravity/magnetic data at variable heights? By adapting the gradient-boosting
method from machine learning to equivalent source processing. Includes a
diagram of the algorithm and an interpolation example showing that the method
is able to fit large amounts of data and still retain spectral content of the
data.](https://github.com/compgeolab/eql-gradient-boosted/raw/2c5f85752bc23b720d80c01243734c61e5f31249/presentations/visual-abstract/visual-abstract.jpg)

# Abstract

The equivalent source technique is a powerful and widely used method for
processing gravity and magnetic data. Nevertheless, its major drawback is the
large computational cost in terms of processing time and computer memory. We
present two techniques for reducing the computational cost of equivalent source
processing: block-averaging source locations and the gradient-boosted
equivalent source algorithm. Through block-averaging, we reduce the number of
source coefficients that must be estimated while retaining the minimum desired
resolution in the final processed data. With the gradient boosting method, we
estimate the sources coefficients in small batches along overlapping windows,
allowing us to reduce the computer memory requirements arbitrarily to conform
to the constraints of the available hardware. We show that the combination of
block-averaging and gradient-boosted equivalent sources is capable of producing
accurate interpolations through tests against synthetic data. Moreover, we
demonstrate the feasibility of our method by gridding a gravity dataset
covering Australia with over 1.7 million observations using a modest personal
computer.
