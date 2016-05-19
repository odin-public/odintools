from __future__ import print_function
from __future__ import absolute_import
import os
import zipfile
import setuptools
import distutils
import markdown
from . import constants
from . import validators

from operator import itemgetter
from odintools import _get_package_root


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
        index = list(filter(lambda i: getattr(self, i, None), indexes))

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
        self.run_command('docs')
        self._upload()


class BuildDocCommand(setuptools.Command):
    description = "Create a devpi-compatible documentation in the 'dist' dir"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        src = os.path.join(_get_package_root(), 'README.md')
        dst_dir = os.path.join(_get_package_root(), 'dist')

        if not os.path.exists(src):
            print("README.md does not exist, skipping documentation generation")
            return

        if not os.path.exists(dst_dir):
            os.mkdir(dst_dir, 0o755)

        doc_file = '{0}.{1}'.format(self.distribution.metadata.get_fullname(), 'doc.zip')

        with open(os.path.join(dst_dir, doc_file), 'wb') as zip:
            doc = zipfile.ZipFile(zip, 'w')

            with open(src) as readme:
                doc.writestr('index.html', markdown.markdown(readme.read()))

            doc.close()
