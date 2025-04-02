---
title: Computer setup
---

<div class="lead">

Most projects developed in the lab will require you to have
a computer with git, a terminal, and Python properly setup.
Below are some **instructions** on how to get started.

</div>

## Git and a terminal

[Git](https://git-scm.com/) is what we use to collaborate on
projects, track a history of changes, and backup to the cloud
(GitHub).

A terminal with a decent shell (like [bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)))
is the primary interface for using git and other command line utilities (LaTeX
compilers, make, etc).

### Windows

You can get both git and a bash-enabled terminal with "Git Bash".
Follow the [Software Carpentry setup instructions](https://carpentries.github.io/workshop-template/#shell)
to get going.

### Linux

You should already have a terminal with bash (look for the "terminal" app).
Git is often already installed as well or you can install it with
your distributions package manager.

On Ubuntu or Linux Mint:

```bash
sudo apt-get install git
```

## Python

<div class="callout">

**DO NOT download Python from [python.org](https://www.python.org)!**
We need a bunch of libraries that don't come pre-installed and can be hard to
install using the official distribution of Python.

</div>

The best way to get setup with Python for your project is by getting a Python
distribution that has the `conda` package manager.
[Anaconda](https://www.anaconda.com/download) is very popular and is good for
some cases but for your project work it will **likely cause more harm than
good** because it comes with too many libraries that we won't need (and is thus
a huge pain to update).

The **recommended** distribution to install for Windows, Linux, and Mac
is [Miniforge](https://conda-forge.org/download/).
This is a minimalist version of Anaconda made by the
[conda-forge](https://conda-forge.org/) team.
It comes only with Python and `conda` (which we use to install other
libraries).

Follow the instructions below to download and setup Miniforge.

### Windows

Download the [latest Miniforge](https://conda-forge.org/download/).
Run the installer and the default should save the installation in a sub folder
`AppData/Local/` within your home folder. For example,
`C:/Users/YOUR_USERNAME/AppData/Local/miniforge3`.
This should create a `miniforge3` folder in your home directory.

<div class="callout">

**Working with Git Bash as well?**
If so, we need to make Git Bash aware of Miniforge so that
you have access to the `conda` package manager.

Add the following initialization code to a file called `.bashrc` in your home
folder (use any text editor you want to do that):

```bash
# Miniforge initialization code
source ~/AppData/Local/miniforge3/etc/profile.d/conda.sh
conda activate
```

If you had Git Bash open, close it and open it again.

</div>

### Testing your install

To test that your setup worked, open Git Bash or the "Miniforge Prompt" program
(on Windows) or your terminal (on Linux).
Run `python` and check if the output looks something like the following (look
for the `packaged by conda-forge` part in particular):

```
Python 3.9.0 | packaged by conda-forge | (default, Nov 26 2020, 07:57:39)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### Installing other Python packages

Now that you have Python installed and properly configured, open Git Bash or
the "Miniforge Prompt" program (on Windows) or your terminal (on Linux).
Then, use `conda` to install the standard Python libraries that we will most
likely be using:

```bash
conda install numpy scipy pandas matplotlib jupyterlab
```

You may also want to install some additional libraries for geophysics:

```bash
conda install xarray netcdf4 pygmt verde harmonica boule bordado
```

You should be good to go from here.

To start JupyterLab, run (it's a good idea to return to your home folder before
doing this by running `cd`):

```
jupyter lab
```
