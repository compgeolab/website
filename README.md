# Souce code for compgeolab.org

[![Build Status](https://img.shields.io/travis/compgeolab/website/master.svg?style=flat-square)](https://travis-ci.org/compgeolab/website)


## Contributing to this site

See [CONTRIBUTING.md](CONTRIBUTING.md).


## Dependencies

You'll need to install Urubu and all it's dependencies to build the site. See
file `requirements.txt` for the complete dependency list. The build works on
Python 2.7 or Python 3.6+.

You can create a conda environment with all required dependencies by running
`conda env create` in the root of the repository. To activate the environment
and run the build use `source activate pinga-site`.


## Compiling the site

1. Open a terminal (`cmd.exe` on Windows) and go to the root of your clone of this
repository.
2. Run `urubu build` to generate the HTML of the website.
3. Run `urubu serve` to start a simple server at the `_build` folder where the
   built HTML files are.  Point your browser to
   [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the site.
   Use `Ctrl+C` to kill the server.

## Adding an image to the Research Highlights section

The carousel on the front page is generated from information in the `_site.yml` file. To
add a new item, place the image in `images/carousel` and add an entry in to `carousel:`
in `_site.yml`. **Important:** Images must be in 16:9 aspect ratio with a width of 600
px.

## Adding a publication

The paper entries are `.md` files in the `papers` folder.
The site theme takes a lot of extra metadata in the post to make the "Info"
section of each entry.

To add a new entry, create the `.md` file in the corresponding folder.
Please, follow the naming conventions used for the other files.

### Metadata for papers

Required:

    title: Geophysical tutorial: Euler deconvolution of potential-field data
    author: uieda, oliveira-jr, barbosa
    date: yyyy-mm-dd
    journal: The Leading Edge
    doi: 10.1190/tle33040448.1
    citation: Uieda, L., V. C. Oliveira Jr, and V. C. F. Barbosa (2014), Geophysical tutorial: Euler deconvolution of potential-field data, The Leading Edge, 33(4), 448-450, doi:10.1190/tle33040448.1
    layout: publication

* `author` should be a list of author ids. The id is the name of the authors
  file in the `people` folder. Authors that are not group members should be
  included in the `authors` field of `_site.yml`.
* `citation` has to be in a single line.

Optional:

    repository: pinga-lab/paper-tle-euler-tutorial
    supplement: 10.6084/m9.figshare.923450
    pdf: paper-tle.pdf
    oa: true
    inreview: true
    related_papers: paper-polynomial-eqlayer-2013,paper-radial3d-gradients-2013
    related_thesis: oliveira-jr-phd

* An entry with `oa: true` will be marked as open-acess.
* `inreview: true` will mark the entry as under peer-review (unpublished).
* `pdf` should be the name of PDF file in the `pdf` folder
* `related_papers` should be a comma-separated list (**no spaces**) of paper
  IDs that are related to this research.
* `related_thesis` the same as `related_papers` but for thesis.


## Adding a new member

Group member pages are the `.md` files in the `people` folder.
To add a new member, create the `.md` file in the corresponding folder with the
**last name** of the person (in lowercase).

### Metadata for members

Required:

    title: Fulano de Tal
    date: yyyy-mm-dd
    position: PhD Student
    institution: Observatório Nacional
    location: Rio de Janeiro, Brasil
    period: 2015-2018
    layout: person

* Use the date that you started on the group.
* `position` should be one of: `PhD Student`, `MSc Student`, `Undergraduate
  Student`
* `period` should be the year when you first started and the year when you left
  the group (use `Present` if you're still a member).

Optional:

    lattes: http://lattes.cnpq.br/8939551682050504
    website: http://www.leouieda.com
    picture: uieda.jpg
    github: leouieda
    email: bla@on.br
    email2: meh@gmail.com
    scholar: http://scholar.google.com.br/citations?user=qfmPrUEAAAAJ
    researcherid: G-3258-2012
    researchgate: https://www.researchgate.net/profile/Leonardo_Uieda
    orcid: 0000-0001-6123-9515
    advisor: barbosa

* `advisor` should be the id of your advisor (the name of his/her file in the
  `people` folder).
* `picture` should be the name of a square image in folder `images/pic`. If
  omitted, will use a default image.


## Adding a new thesis

We also have a page with all theses defended by group members.
To add a new one, create a new `.md` file in the `thesis` folder. The file name
should be your page name plus the degree all in lowercase, e.g. `uieda-msc.md`.
You should also place a PDF version of the thesis with the same name in the
`pdf` folder.

### Metadata for theses

Required:

    title: Forward modeling and inversion of gravitational fields in spherical coordinates
    author: uieda
    advisor: barbosa
    date: yyyy-mm-dd
    period: 2011-2016
    institution: Observatório Nacional
    level: PhD
    pdf: uieda-phd.pdf
    sucupira: 154585
    layout: publication

* `author` should be your author ids. The id is the name of the authors
  file in the `people` folder.
* `advisor` should be the author id of the thesis advisor.
* `level` should be one of: `PhD`, `MSc`, or `Undergraduate`.
* `sucupira` is the ID of your thesis on the [Sucupira
  platform](https://sucupira.capes.gov.br). You can get the ID by search for
  your thesis [here](https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/trabalhoConclusao/listaTrabalhoConclusao.jsf),
  then get the ID number from the end of the link to your thesis. For example,
  the ID for the link
  `https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/trabalhoConclusao/viewTrabalhoConclusao.jsf?popup=true&id_trabalho=3627205`
  is `3627205`.

Optional:

    repository: leouieda/phd-thesis
    doi: 10.6084/m9.figshare.923450
    related_papers: paper-polynomial-eqlayer-2013,paper-radial3d-gradients-2013
    related_thesis: oliveira-jr-phd

* `related_papers` and `related_thesis` are the same as for a paper.

## License

[![Creative Commons
License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
This work is licensed under a
[Creative Commons Attribution 4.0 International
License](http://creativecommons.org/licenses/by/4.0/).
