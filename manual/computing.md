---
title: Setting up your computer
---

Most projects developed in the lab will require you to have
git, a terminal, and Python properly setup on your computer.
Below are some instructions on how to do this.

## Git and a terminal

[Git](https://git-scm.com/) is what we use to collaborate on
projects, track a history of changes, and backup to the cloud
(GitHub).

A terminal with a decent shell (e.g., bash) is the primary
interface for using git and other command line utilities
(LaTeX compilers, make, etc).

### Windows

You can get both git and a bash-enabled terminal with "Git Bash".
Follow the [Software Carpentry setup instructions](https://carpentries.github.io/workshop-template/#shell)
to get going.

### Linux

You should already have a terminal with bash (look for the "terminal" app).
Git is often already installed as well or you can install it with
your distributions package manager.

On Ubuntu:

```bash
sudo apt-get install git
```

## Python

**DO NOT** download Python from [www.python.org](https://www.python.org)!

The best way to get setup with Python for your project is
by getting a Python distribution that has the `conda` or `mamba`
package managers. Anaconda itself (which you likely have from
one of Leo's classes) is good for some cases but for your
project work it will likely cause more harm than good because
it comes with too many libraries that we won't need (and is thus
a huge pain to update).

The recommended distribution to install for Windows, Linux, and Mac
is [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge).
This is a minimalist version of Anaconda made by the
[conda-forge](https://conda-forge.org/) team. It comes only with Python
and `mamba` (which we use to install other libraries).

Follow the instructions below to download and setup Mambaforge.

### Windows

Download the [latest Mambaforge](https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Windows-x86_64.exe).

Run the installer and the default should save the installation in a sub folder `AppData/Local/` within your home folder.
For example,  `C:/Users/YOUR_USERNAME/AppData/Local/mambaforge`.

This should create a `mambaforge` folder in your home directory
(open Git Bash and run `cd` to get to your home).

Now we need to make Git Bash aware of Mambaforge so that
you have access to the `mamba` package manager.

Run the commands below on Git Bash.

Add the following initialization code to a file called `.bashrc` in your home folder:

```bash
# Mambaforge initialization code
source ~/AppData/Local/mambaforge/etc/profile.d/conda.sh
conda activate
```

After that, close Git Bash and open it again.
To test that your setup worked, run `python` and
check if the output looks something like the following:

```
Python 3.9.0 | packaged by conda-forge | (default, Nov 26 2020, 07:57:39)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Also try running `mamba` and check that the output is something like:

```
usage: mamba [-h] [-V] command ...

conda is a tool for managing and deploying applications, environments and packages.

Options:

positional arguments:
  command
    clean        Remove unused packages and caches.
    compare      Compare packages between conda environments.
    config       Modify configuration values in .condarc. This is modeled after the git config command. Writes to the user .condarc file (/home/leo/.condarc) by default.
    create       Create a new conda environment from a list of specified packages.
    help         Displays a list of available conda commands and their help strings.
    info         Display information about current conda install.
    init         Initialize conda for shell interaction. [Experimental]
    install      Installs a list of packages into a specified conda environment.
    list         List linked packages in a conda environment.
    package      Low-level conda package utility. (EXPERIMENTAL)
    remove       Remove a list of packages from a specified conda environment.
    uninstall    Alias for conda remove.
    run          Run an executable in a conda environment. [Experimental]
    search       Search for packages and display associated information. The input is a MatchSpec, a query language for conda packages. See examples below.
    update       Updates conda packages to the latest compatible version.
    upgrade      Alias for conda update.
    repoquery    Query repositories using mamba.

optional arguments:
  -h, --help     Show this help message and exit.
  -V, --version  Show the conda version number and exit.

conda commands available from other packages:
  env
```

Now that you have Python installed and properly configured,
use `mamba` to install the standard Python libraries that
we will most likely be using:

```bash
mamba install numpy scipy pandas matplotlib xarray netcdf4 make \
    jupyter jupyterlab pyproj verde harmonica boule pooch
```

You should be good to go from here. To start JupyterLab, run
(it's a good idea to return to your home folder before doing
this by running `cd`):

```
jupyter lab
```
