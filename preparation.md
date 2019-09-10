# Preparation

## Format

The tutorial consists of lecture segments, followed by hands-on
exercises.  We *strongly encourage* you to bring a laptop with all the
required packages installed in order to participate fully.

## Software required

- Python

  If you are new to Python, please install the
  [Anaconda distribution](https://www.continuum.io/downloads) for
  **Python version 3** (available on OSX, Linux, and Windows).
  Everyone else, feel free to use your favorite distribution, but
  please ensure the requirements below are met:

  - `python` >= 3.6
  - `numpy` >= 1.12
  - `scipy` >= 1.0
  - `matplotlib` >= 2.1
  - `scikit-image` >= 0.15
  - `itk` >= 4.1

  Please see "Test your setup" below.

- **ITK**

  ITK is an open-source toolkit for multidimensional image analysis.
  If you are using Anaconda, it is easy to install ITK using the
  [conda-forge](https://conda-forge.org/) repository, through the
  following command:

  `$ conda install -c conda-forge itk`

  You can also use the PyPI package:

  `$ pip3 install --upgrade itk`

- Jupyter

  The lecture material includes Jupyter notebooks.  Please follow the
  [Jupyter installation instructions](http://jupyter.readthedocs.io/en/latest/install.html),
  and ensure you have version 4 or later:

  ```bash
  $ jupyter --version
  4.4.0
  ```

  Also activate Jupyter Widgets:

  ```
  pip install -q ipywidgets
  jupyter nbextension enable --py --sys-prefix widgetsnbextension
  ```

## Download lecture material

1. [Install Git](https://git-scm.com/downloads)
2. Clone the repository at
   [https://github.com/imagexd/2019-tutorial-skimage](https://github.com/imagexd/2019-tutorial-skimage)

We may make editorial corrections to the material until the day before
the workshop, so please execute `git pull` to update.

## Using a conda environment

We created the file `environment.yml`, available on the lecture material, to ease
the process of creating an environment ready for this tutorial. For doing that, you
can use the command `conda env`:

`$ conda env create -f environment.yml`

Then, to activate this environment,

` $ conda activate imagexd19_skimage`

To come back to your master environment,

`$ conda activate`

More on conda environments at: [[conda's user guide]](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

## Test your setup

Please switch into the repository you downloaded in the previous step,
and run `check_setup.py` to validate your installation.

On my computer, I see (but your version numbers may differ):

```
[✓] scikit-image  0.15.0
[✓] numpy         1.14.5
[✓] scipy         1.1.0
[✓] matplotlib    2.2.2
[✓] notebook      5.4.0
```
**If you do not have a working setup, please contact the instructors.**
