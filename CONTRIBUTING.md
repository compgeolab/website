# Contributing to this website

## What you'll need

* A GitHub account
* Install git (on Windows, I recommend installing the "Git for Windows SDK"
  from https://git-for-windows.github.io/)
* Install Python, preferably with the Anaconda distribution
* Install [Nēnē](https://nene.leouieda.com/), which is what we use to build the
  website

Windows users: when I say "terminal" below, I will mean this "Git Bash" shell.

## Getting a copy of the site

First, click on the "fork" button in the
[compgeolab/website](https://github.com/compgeolab/website)
repository to grab a copy of the repository to your personal account.
**You only need to do this once**.

Then you can clone your fork of the site to your personal computer so you can
edit the files. In a terminal, type:

    git clone git@github.com:YOUR_USER_NAME/website.git

This will create a `website` folder in the current directory holding the
website code.

## Build and viewing the HTML

To generate the website HTML and view it in your default web browser, run this
in a terminal (from inside the `website` folder!):¨

    nene --serve

This command will build the HTML, start a local server, and open your browser
with the locally served page.
Every time you edit the source files, it will rebuild and update automatically.

This will keep your terminal busy (that's normal). When you're done, type
`CTRL+C` in the kill the local server.

### Update your local copy

If you've already done the above before, your personal copy is probably out of
sync with the original repository at
[compgeolab/website](https://github.com/compgeolab/website).

To update your local copy and fork, first you'll need to register the original
repository. In your local copy, run:

    git remote add upstream git@github.com:compgeolab/website.git

This will register the original repository as a source. Then run the following
to pull in changes from the original:

    git checkout main
    git pull upstream main

And finally, update your fork:

    git push origin main

Now your local copy and fork should be updated.

## Making changes

Before you make changes, you should first create a "branch" so that your
changes don't break the main site. To do this, run:

    git checkout main
    git checkout -b NAME_OF_YOUR_BRANCH

You can make as many branches as you like, so don't worry.
Once you have your branch checked out, changes you make to the files in your
local copy will be committed to your branch.

After you're satisfied with your changes, you should mark them for addition
with:

    git add FILE1 FILE2 FILE3 ...

And then make a commit with those changes:

    git commit -m "Message describing your changes"

Now you can push your local changes to your fork by running:

    git push -u origin NAME_OF_YOUR_BRANCH

At this point, your changes are registered in your personal fork on GitHub. Now
we have to integrate them into the main website code.

## Making a Pull Request

Go to the GitHub page for the original repository
[compgeolab/website](https://github.com/compgeolab/website).
There should be a line there with your branch and a green "Compare & pull
request" button.

Click on the button to open a new pull request.

Fill the text box with a description of the changes you made and submit the
pull request.

Now, someone will review and merge your pull request. When that's done, the
website will be updated automatically.

## Adding yourself to the website

The [Team page](https://compgeolab.org/team) is built from the information in
`team/people.yml`.
To add yourself to the website, create a new entry in that file under the
appropriate category.

* Use the existing entries as reference.
* Feel free to add as much or as little information as you want.
* The profile picture is captured automatically from your GitHub account.
* Be aware of white pace! It needs to be consistent.
