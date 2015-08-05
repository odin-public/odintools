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

## Installing a package built with odintools

Besides ~/.pip/pip.conf file with the following contents:

```bash
mkdir ~/.pip; cat > ~/.pip/pip.conf <<EOF
[global]
index-url = http://pypi.aps.sw.ru/odin/pypi/+simple/
trusted-host = pypi.aps.sw.ru
EOF
```

you'll need a setuptools/disutils configuration file:

```bash
cat > .pydistutils.cfg <<EOF
[easy_install]
index-url = http://pypi.aps.sw.ru/odin/pypi/+simple/
trusted-host = pypi.aps.sw.ru
EOF
```

Pydistutils is required because `setup_requires` line in `setup()` call is processed
by setuptools, not pip, so it needs a separate configuration.

[python-packaging]: https://rnd-teamwork.sw.ru/x/1x-N
