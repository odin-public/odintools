import re
import distutils


__all__ = ['validate_version']


validators = {}


def validator(index):
    def decorator(f):
        def wrapper(version):
            match = f(version)

            if match is None:
                raise distutils.errors.DistutilsOptionError(
                    "Invalid version format: '{0}', please consult "
                    "https://confluence.int.zone/x/1x-N".format(version)
                )

        validators[index] = wrapper

        return wrapper
    return decorator


@validator('dev')
def validate_dev(version_string):
    r = re.compile(r'^([0-9]*\.)*dev[0-9]*$')

    return r.match(version_string)


@validator('prod')
def validate_prod(version_string):
    r = re.compile(r'^([0-9]*\.)*[0-9]*$')

    return r.match(version_string)


def validate_version(index, version_string):
    try:
        return validators[index](version_string)
    except KeyError:
        raise distutils.errors.DistutilsOptionError("Unknown index: {0}".format(index))
