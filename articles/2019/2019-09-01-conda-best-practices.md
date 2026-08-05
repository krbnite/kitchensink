---
title: Conda Best Practices
layout: post
tags: conda python environments reproducibility
date-note: exact day unknown; September 2019 inferred from CVB writing-sample notes
---

# Conda Best Practices

## 1. Use Conda as a primary tool for package and environment management

People often think of `conda` and `pip` as similar tools -- in the same
category of functionality.   However, `conda` is more versalile than `pip`: 
it is not only an installer, but a full-fledged environment manager. By itself,
`pip` is just an installer.  It will install whatever you tell it to, for sure,
but that's not necessarily a good thing as it can often lead to broken
environments!  

A more direct comparison to `conda` would be to consider `pip` and `virtualenv`
as a tool suite.  (To address this shortcoming, pipenv was created, among other 
solutions. However, for data science tasks, `conda` is still the leader in this
area.)

Importantly, `conda` will not create a broken environment: its installs 
may take longer, but only because it goes over each dependency (and dependencies 
of dependencies in the dependency stack) to discover and ensure a build that 
has full package compatibility.  If `conda` cannot do find a compatible solution,
it will discontinue the build and issue a warning and some advice.  On the other 
hand, pip will just download whatever you specify and overwrite/replace anything that 
gets in its way; this is what leads to a broken environment.


## 2. If possible, only install packages with `conda install`

This will result in the most reproducible, bug-free environments possible.

However, sticking to this best practice can be tricky.

Despite having access to 1000's of packages (if not directly, 
then through channels such as `conda-forge` and `bioconda`), `conda install` can't 
compete with the 100's of 1000's of packages available to `pip install`.  This
can be frustrating and lead data scientists into bad habits, such as favoring
`pip` (without at least adopting `virtualenv` along with it) or developing 
arbitrary conda/pip install patterns (more on this below).

Another weakness of `conda` that can cause some disillusionment is that `conda` 
often lags behind `pip` on a package's version (e.g., at the time of writing, `conda` 
only had up to TF 2.0, whereas pip had access up to TF 2.3).

In reality, at least in my experience, you are going to probably have to use
`pip` for one or more packages.  However, this rule will help maintain your
sanity.  Make sure to search the various conda channels
and think about whether you really need the latest version of a package (often
an environment can be built if you allow for some flexibility).

If the package or the package version you require really isn't available to
`conda install`, then set it aside and continue building the environment
by conda installing other packages you require.



## 3. If `conda install` doesn't work, do not necessarily go straight to pip

For projects available on PyPI (i.e., packages you can install with pip),  
`conda skeleton` may be able to produce a build recipe that can be used to 
build a conda package. 

You will find this recommended as a best practice by some practitioners,
though others in the field dislike and recommend against this approach.  

Personally, up until a few weeks ago, I had never used `conda build` or 
`conda skeleton`.  When I tried to do so for TensorFlow (wanted 2.2, but
conda currently only goes up to 2.0), this approach failed miserably and
was nigh impossible to find much help online.  So... Keep it in mind, but
it's probably not worth losing sleep over (especially if using pip for 
the one or two packages you need doesn't break your environment).

If you cannot get this approach to work (or deem it to be too complicated 
and/or overkill), then set it aside and continue building the environment
by conda installing other packages you require.


## 4. Use `pip` if you must, but only after all `conda install`s


Let's face it: "if you must" usually translates to something like "if you're in 
a hurry" or  "if you're feeling lazy and it doesn't seem to really break 
anything." However, oftentimes you simply have to.

The most import rule of using `pip` with `conda` (if you care about unbroken,
reproducible environments) is to  make sure not to use them in a random fashion, like 
"conda this, pip that, conda, pip, conda, conda, pip."

If you are following these best practices in order so far, then presumably you 
have conda installed whatever packages could be conda installed (and perhaps you
used `conda skeleton` or `conda build` as well).  

After having created your environment as completely as possible with conda tools, 
you may then move onto `pip install` using `--upgrade-strategy only-if-needed` (this 
is actually pip's default, so the point here is: don't change it!).

Pip can dramatically alter your environment without asking for permission and without
concern for complete consistency and cross-functionality across the environment.  
It is usually a good idea to first clone your environment and do a test run.

```
conda create -n testEnv --clone myEnv
conda activate testEnv
pip install <pkg>
```

This way you can see what kind of changes are made without fear of destroying
anything.  If everything looks ok, then you can go ahead and finish up
buiding your environment:

```
conda deactivate
conda env remove -n testEnv
pip install <pkg>
```

## 5. Leave the Root Environment Alone:  Create an Environment for Each Project
Do yourself a favor and get into the habit of building new environments for each project
you work on.  It's easy to get into the very bad habit of developing projects in the
root environment.  This is the type of habit that seems ok until the second it's not:
at one point, you will almost definitely decide to `conda install` or `pip install`
something that upgrades and downgrades things in a way that breaks something, somewhere
in one of your projects.

Importantly, if you get in the habit of using the root environment, you will inevitably 
end up engaging in some randomized pip-conda-pip-pip-conda installation sequence -- in violation
of the aforementioned best practices.  This will often land you in a broken root environment.

If you do find yourself in this position, it's good to know that conda version controls
your environments -- and that you can revert to a previous state.

```
# See previous env versions
conda list --revisions

# Revert/rollback to prior env state
conda install --revision v  # v: revision number
```


By getting into the good habit of creating non-root environments, you will be less likely 
to make a randomized pip-conda mistake.  

If in the middle of a project you realize you need a new package, the best practice is to create 
a new environment to test out.  In this case, if you deem that a `pip install` is necessary,
then you can simply clone the environment (assuming you've followed the aforementioned best
practices):

```
conda create -n testEnv --clone myEnv
conda activate testEnv 
pip install <pkg>
```

If everything is safe, then you can go ahead and safely modify the project's environment.  
If something breaks, you figure out if there is a better solution.  In either case, you can 
delete the test environment afterwards:

```
conda deactivate
conda env remove -n testEnv
```

But what if you want to `conda install` a package?  Cloning the environment will not do if
the environment has had a `pip install`.  Instead, you must have a way to recreate the
environment in a more controlled, programmatic fashion.

This brings us to environment creation files (next section), which you can use to build a new 
environment following best practices:
1. create new environment using conda requirements file
2. conda install new packages to test compatibility, etc
3. finish building environment with pip requirements file


------------------------------------------------------------------


## 6. Environment Requirements/Creation Files

If your project is supposed to run somewhere else, on someone else’s machine, etc, then do everyone a favor and create the environment text file(s).

People familiar with pip know this as a requirements.txt file, which is often created using the command pip freeze > requirements.txt.  Note that this will capture any and all pip-installed packages in the environment, so if you’re starting from the Anaconda root instead of the Miniconda root, the file will be relatively bloated.   If you can manage, it’s sometimes better to just manually create the file.  For example, if you only use numpy and pandas in the code, then just create a file listing those two packages (their dependencies will automatically be taken care of); this is much easier on the eyes than the results of pip freeze.

The equivalent conda command is conda list > conda.txt.

So, at a lazy minimum, if you want people to be able to recreate your environments, you want to provide them with the conda and pip installation files generated by these commands:

conda list > conda-requirements.txt

pip freeze > pip-requirements.txt

However, at a less lazy minimum, you want to manually create these two files.

The solution that I think is best is creating a hybrid requirements file, like this:

conda.yaml
name: myAwesomeProject
channels:
  - conda-forge
dependencies:
  - python=3.6
  - numpy>=1.18
  - pandas=0.25
  - pip:
    - tensorflow-gpu=2.3

Then you can create a conda environment from the file: conda create --require conda.yaml








## 7.  Restore environments, if necessary


Above, I spoke about damaging an environment and the best practices to avoid doing so…. Well, nobody’s perfect and you might just destroy your environment.
You’re in luck!  Apparently conda creates a history of your environments (like a git repo, basically), so you can rollback environment changes to a previous version.
Check out your env history like so: conda list --revisions
To restore a prior env version: conda install --revision=<revNum>
