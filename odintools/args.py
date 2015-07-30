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
