from pbr.packaging import _get_version_from_git


def ost(dist, attr, value):
    print("ost({}, {}, {})".format(dist, attr, value))
    print("Version: {}".format(_get_version_from_git()))
