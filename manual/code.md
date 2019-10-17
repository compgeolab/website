---
title: Coding and Software
date: 2019-09-15
layout: manual
pager: true
---

# Coding Standards

Code should avoid being "too clever."  This means things like avoiding clever abuses of
language (for instance, utilizing lack of closures in python to remove the need for a
variable) and algorithms that cut corners in the interest of marginal time savings.

In general, we want to balance all needs for performance with needs for clarity and
maintainability. Readability and maintainability are the key functionalities we need to
emphasize, as this will ensure the code can remain useful beyond the original scope of
the project.

Tests should be considered mandatory for new functionality *and* bug fixes to lab
software. These tests should be part of automated testing suites.

For Python code, we use [black](https://github.com/psf/black) to automatically format
code. Let it do it's job and don't worry about formatting.

Documentation must be added with any new set of code, and should be documented in a way
that is accessible to newcomers to a given project. Where possible, worked examples
should be provided.

# Commenting

Comments should be considered encouraged, but not necessary. Code should be as
self-describing as possible; where complex optimizations are present, comments
should enable an individual to understand shortcuts and reasoning.

Whenever possible, citations to algorithms (whether from papers or URLs such as
Stack Overflow) must be included in comments close to that section of the code.
(Note that in the specific case of Stack Overflow, code and answers are
subject to licensing restrictions, which in practice will likely not impact
their utilization but which must be acknowledged.)

Whenever developing in Python, docstrings should be added to *all* public functions.
These must at a minimum cover all parameters and expected output, along with a
description of the function and citation to methods implemented.

# Licensing

All code generated in the lab should be open-source with a permissive (non-copyleft)
license (MIT, BSD, etc).
If contributions to upstream copyleft projects are made, those contributions
can be licensed in accordance with the upstream project license.

Importantly, in the lab we should cultivate an atmosphere of respect for
licensing terms and ensuring that we are at all times in compliance with those
terms. Our preferred license is
[BSD 3-clause](https://opensource.org/licenses/BSD-3-Clause).
For further discussion see
[Stodden (2008)](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?reload=true&arnumber=4720221).

# Languages

In general, the lab uses Python for most of its software. This can include web apps as
well as analysis and visualization software like
[Fatiando a Terra](https://www.fatiando.org/).
Experimenting with Julia and other languages is of course acceptable and even desirable.
For optimized code that needs to be fast, the first preference is Numba, then Cython,
and finally C.

# Using Other Code

In general, using external code in lab projects is a balance between a few factors.
If a large external project provides a small amount of functionality
that would be used in a lab project which is to be distributed widely, the
difficulty of the external library to install and keep up with (i.e., API
changes) must be accounted for versus the difficulty of either "vendoring" the
functionality (license-permitting) or re-implementing.
In general we want to use external code for functions that are either core functionality
of our projects (numpy, lapack, etc) and for difficulty but non-core functions of our
projects.

If the dependency is a small, lightweight dependency, typically it's better to
utilize it than to re-implement the functionality.  But, for
difficult-to-install libraries or libraries where utilized functionality
outweighs the overhead of installation, it's better to bring it up for a
discussion.

# Project Leadership

When software is developed as a result of funded activity, the leadership
directions will be set collaboratively during the proposal writing process and
then subsequently between lab members and Leo.
For projects which are externally developed, leadership for the project as a whole will
be conducted as decided by the broader community.

Decisions regarding strategic direction for software projects (including
algorithmic strategies) will be made collaboratively.

For technical directions on lab-developed software, we operate by
["lazy consensus"](https://rave.apache.org/docs/governance/lazyConsensus.html),
which can be conducted via the Slack chat.
