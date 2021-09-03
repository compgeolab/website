---
title: "Gradient-boosted equivalent sources"
date: 2021-02-25
author: santisoler, uieda
repository: https://github.com/compgeolab/eql-gradient-boosted
journal: Geophysical Journal International
layout: publication
tags: gravity
doi: 10.1093/gji/ggab297
preprint: 10.31223/X58G7C
supplement: 10.6084/m9.figshare.13604360
citation: "Soler, S.R. and Uieda, L., 2021. Gradient-boosted equivalent sources, Geophysical Journal International, doi:10.1093/gji/ggab297"
---

# About

We present the gradient-boosted equivalent sources: a new methodology for
interpolating very large datasets of gravity and magnetic observations even on
modest personal computers, without the high computer memory needs of the
classical equivalent sources technique. This new method is inspired by the
gradient-boosting technique, mainly used in machine learning solutions.

![Visual abstract](/images/eql-gradient-boosted.jpg)

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
