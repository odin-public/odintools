import os
import setuptools
import distutils
import constants
import validators

from operator import itemgetter


class PublishCommand(setuptools.Command):
    description = "Publish package to Odin pypi repository"
    command_name = 'publish'
    user_options = [
        ('dev', None,
         "Create a development package and publish it on the Odin repo",
         {'index': 'dev'}),
        ('prod', None,
         "Create a production package and publish it on the Odin repo",
         {'index': 'prod'}),
    ]

    def initialize_options(self):
        self.index = None
        self.prod = None
        self.dev = None

    def finalize_options(self):
        indexes = map(itemgetter('index'),
                      map(itemgetter(3),
                          filter(lambda op: len(op) == 4 and 'index' in op[3],
                                 self.user_options)))
        index = filter(lambda i: getattr(self, i, None), indexes)

        if len(index) != 1:
            raise distutils.errors.DistutilsOptionError("Please supply either "
                                                        "'--dev' or '--prod' parameter")

        self.index = index[0]

    def _validate_version(self):
        ver = self.distribution.metadata.version

        validators.validate_version(self.index, ver)

    def _upload(self):
        odin_password = os.environ.get(constants.PYPI_PASSWORD_VAR)

        if not odin_password:
            self.warn("Environment variable '{0}' not set, skipping upload"
                      .format(constants.PYPI_PASSWORD_VAR))
            return

        self.spawn('devpi use {0}'
                   .format(constants.PYPI_REPO_BASE)
                   .split())
        self.spawn('devpi login {0} --password {1}'
                   .format(constants.PYPI_REPO_USER, odin_password)
                   .split())
        self.spawn('devpi use {0}'
                   .format(self.index)
                   .split())
        self.spawn('devpi upload --from-dir ./dist'
                   .split())

    def _set_version(self):
        if not hasattr(self.distribution.metadata, 'version_getter'):
            raise distutils.errors.DistutilsOptionError(
                "Please supply a 'version_getter' callback")

        version = self.distribution.metadata.version_getter

        self.distribution.metadata.version = version(self.index)

    def run(self):
        self._set_version()
        self._validate_version()
        self.run_command('sdist')
        self._upload()
