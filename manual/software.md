---
title: Software produced by the lab
---

The following are guidelines to be followed when producing software tools as
part of your work at the lab.

## Licensing

* We value respect for licensing terms and ensuring that we comply with them at
  all times.
* All code generated in the lab should be open-source with a permissive
  (non-copyleft) license (MIT, BSD, etc).
* Our preferred license is [BSD 3-clause](https://opensource.org/licenses/BSD-3-Clause).
* If contributions to upstream copyleft (GPL, etc) projects are made, those
  contributions can be licensed in accordance with the upstream project license.
* For further discussion see [Stodden (2008)](https://doi.org/10.1109/MCSE.2009.19).

## Project leadership

* When software is developed as a result of funded activity, the leadership
  directions will be set collaboratively during the proposal writing process and
  between lab members and Leo.
* For externally developed projects, leadership is as decided by the broader
  community.
* Decisions regarding strategic direction for software projects (including
  algorithmic strategies) will be made collaboratively.
* For technical directions on lab-developed software, we operate by
  ["lazy consensus"](https://rave.apache.org/docs/governance/lazyConsensus.html).

## External projects

* We strive to be good "citizens" of the broader open-source community.
* We encourage lab members to contribute upstream to open-source projects.
* Projects developed with external collaborators (e.g.,
  [Fatiando a Terra](https://www.fatiando.org)) should have their discussions
  held openly. This can help discourage the notion that projects developed by
  lab members are not community projects.
* For more discussion about this topic, see Matt Turk's paper
  [Scaling a Code in the Human Dimension](https://arxiv.org/abs/1301.7064).

## Languages

* Use Python for most software.
* Experimenting with Julia and other languages is acceptable and even desirable.
* For code that needs to be optimized, the first preference is (in order):
  Numba, then Cython, and finally C.

## Coding standards

* Code should avoid being "too clever", for example clever abuses of languages
  and algorithms that cut corners in the interest of marginal time savings.
* Clarity and maintainability take precedence over performance to ensure that
  the code can remain useful beyond the original scope of the project.
* Tests should be considered mandatory for new functionality and bug fixes.
  These tests should be part of automated testing suites.
* Use [black](https://github.com/psf/black) to automatically format Python code.
* Documentation must be added with any new code and should be accessible to
  newcomers. Include examples whenever possible.
* Comments (not including markdown cells in notebooks) are encouraged but not
  necessary. Code should be as self-describing as possible. Where complexity
  is inevitable, comments should allow anyone to  understand the shortcuts and
  reasoning.
* Include citations to algorithms whenever possible, including links to online
  resources.
* Docstrings should be added to all functions and classes in Python code.
