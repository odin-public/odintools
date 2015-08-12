odintools - Odin Setup Tools
============================

This library helps to automate continuous delivery processes adopted in Odin.
More information: [Python packaging][python-packaging]


## Installation

Current version is at an early stage of development, so you may want to
install it in the `develop` mode in your virtualenv:

```bash
$ python setup.py develop
```


## Usage

Ensure that you have `odintools` in your `setup_requires` list and pass
`odintools=True` as a keyword argument in the `setup()` call:

```python
from setuptools import setup

setup(
    setup_requires=['odintools'],
    odintools=True,
    ...
)
```

After you enable odintools in the setup.py file you can use new commands
provided by it:

```bash
$ python setup.py publish --dev
```


Pydistutils is required because `setup_requires` line in `setup()` call is processed
by setuptools, not pip, so it needs a separate configuration.
