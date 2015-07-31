import os
import commands
import distutils


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
    })


def version_getter(dist, attr, getter):
    if not callable(getter):
        raise distutils.errors.DistutilsSetupError(
            "Value passed to 'version_getter' must be callable, got {1}".format(type(getter))
        )

    index = os.environ.get('DEVPI_INDEX')
    dist.metadata.version_getter = getter()

    if index:
        dist.metadata.version = dist.metadata.version_getter(index)
