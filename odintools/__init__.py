def version(ver, suffix=None):
    def version_setter(index):
        _suffix = suffix

        if _suffix is None:
            _suffix = '0'

        if index == 'dev':
            _suffix = 'dev' + _suffix

        return '{0}.{1}'.format(ver, _suffix)

    return version_setter
