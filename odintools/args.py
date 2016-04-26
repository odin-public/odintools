from __future__ import absolute_import
from . import commands
import distutils

from odintools import _get_version_file


def odintools(dist, attr, value):
    if bool(value) != value:
        raise distutils.errors.DistutilsSetupError(
            "{0} attribute must be boolean, got {1}".format(attr,
                                                            type(value))
        )

    if not value:
        return

    dist.cmdclass.update({
        'publish': commands.PublishCommand,
        'docs': commands.BuildDocCommand,
    })


def version_getter(dist, attr, make_getter):
    if not callable(make_getter):
        raise distutils.errors.DistutilsSetupError(
            "Value passed to 'version_getter' must be callable, got {1}".format(
                type(make_getter))
        )

    try:
        with open(_get_version_file()) as ver:
            version = ver.read().strip()
    except IOError:
        version = None

    dist.metadata.version_getter = make_getter()
    dist.metadata.version = version
