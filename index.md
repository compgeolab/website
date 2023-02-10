---
custom_page_title: Computer-Oriented Geoscience Lab
banner_title: "Geophysical research <br> powered by open-source software"
banner_subtitle: |
  At the <strong>Computer-Oriented Geoscience Lab</strong>, we design
  state-of-the-art computational tools for the Geosciences.
  <strong>Source code included.</strong>
banner_downward_link: "#about-us"
template: index.html
---

{% from "macros.html" import figure, video %}

<section class="row gy-5 gx-5">
<div class="col-md-7">

## About us

The **CompGeoLab** is a research group based at the
[{{ config.location.university }}'s {{ config.location.school }}][uol].
We are experts in solving **inverse problems** in the field of **Geophysics**.
For example, determining the inner density distribution of the Earth from
measured disturbances in the Earth's gravity field.
These are the main tools used by geoscientists to **image the inside** of the
Earth and other planets.

We also specialize in building **open-source scientific software**.
Our team works on [several tools and projects]({{ site["software/index"].path|relative_to(page.path) }}), both developing
tools in-house and contributing across the larger scientific ecosystem.

<div class="mt-5">
<a class="btn clab-button mb-4 me-2" href="{{ site["team/index"].path|relative_to(page.path) }}">Meet the team</a>
<a class="btn clab-button-outline mb-4 me-2" href="{{ site["research/index"].path|relative_to(page.path) }}">Our research</a>
<a class="btn clab-button-outline mb-4 me-2" href="{{ site["manual/index"].path|relative_to(page.path) }}">Lab Manual</a>
<a class="btn clab-button-outline mb-4 me-2" href="{{ site["contact/index"].path|relative_to(page.path) }}">Work with us</a>
</div>

</div>
<div class="col-md-5">

{{ video(src="../images/planting-inversion.mp4", caption="The planting method for solving the inverse problem of estimating density from observed gravity disturbances.", style="display: block; margin: 0 auto; width: 100%;") }}

</div>
</section>

<hr class="section-separator">

[uol]: https://www.liverpool.ac.uk/earth-ocean-and-ecological-sciences/
