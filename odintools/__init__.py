import os


def version(ver, suffix=None):
    def version_setter(index):
        _suffix = suffix

        if _suffix is None:
            _suffix = '0'

        if index == 'dev':
            _suffix = 'dev' + _suffix

        version = '{0}.{1}'.format(ver, _suffix)

        _write_version_file(version)

        return version

    return version_setter


def _get_version_file():
    return os.path.join(_get_package_root(), 'VERSION')


def _get_manifest_file():
    return os.path.join(_get_package_root(), 'MANIFEST.in')


def _get_package_root():
    return os.getcwd()


def _write_version_file(version):
    with open(_get_version_file(), 'w') as f:
        f.write(version)

    if not os.path.exists(_get_manifest_file()):
        mode = 'w+'
    else:
        mode = 'r+'

    with open(_get_manifest_file(), mode) as f:
        if not any(filter(lambda s: 'VERSION' in s, f.readlines())):
            f.seek(0, os.SEEK_END)
            f.write("\ninclude VERSION")
