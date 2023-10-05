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
  - name: Lab Manual
    id: manual/index
template: index.html
---

{% from "macros.html" import figure, video %}

## About us

The **CompGeoLab** is a research group based at the
[{{ config.location.university }}][usp].
We are experts in solving **inverse problems** in the field of **Geophysics**.
For example, determining the inner density distribution of the Earth from
measured disturbances in the Earth's gravity field.
These are the main tools used by geoscientists to **image the inside** of the
Earth and other planets.

We also specialize in building **open-source scientific software**.
Our team works on [several tools and projects]({{ site["software/index"].path|relative_to(page.path) }}), both developing
tools in-house and contributing across the larger scientific ecosystem.

{{ video(src="../images/planting-inversion.mp4", caption="The planting method for solving the inverse problem of estimating density from observed gravity disturbances.", style="display: block; margin: 0 auto; width: 50%;") }}

[usp]: https://www.iag.usp.br/
