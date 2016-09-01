import os
import sys

from setuptools import setup, find_packages

__path__ = os.path.split(__file__)[0]
PACKAGE_NAME = 'odintools'


def long_description():
    return open(os.path.join(__path__, 'README.md')).read()


def install_requires():
    if sys.version_info < (2, 7):
        return ['importlib>=1.0', 'markdown==2.6.2']
    else:
        return ['markdown==2.6.6']


def version():
    def version_file(mode='r'):
        return open(os.path.join(__path__, 'version.txt'), mode)

    if os.getenv('TRAVIS'):
        major_version = '0.2'
        with version_file('w') as verfile:
            verfile.write('{0}.{1}'.format(major_version, os.getenv('TRAVIS_BUILD_NUMBER')))
    with version_file() as verfile:
        data = verfile.readlines()
        return data[0].strip()


try:
    # when launched during the build process
    from odintools.commands import BuildDocCommand

    x = BuildDocCommand
    cmdclass = {'docs': x}
except:
    # when installed in production
    cmdclass = {}

setup(
    name=PACKAGE_NAME,
    author='apsliteteam',
    author_email='aps@odin.com',
    description='Odin setuptools extensions',
    long_description=long_description(),
    url='http://aps.odin.com',
    version=version(),
    license='Other/Proprietary License',
    classifiers=[
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords=['setup', 'distutils'],
    packages=find_packages(),
    install_requires=install_requires(),
    entry_points={
        'distutils.setup_keywords': [
            'odintools = odintools.args:odintools',
            'version_getter = odintools.args:version_getter',
        ]
    },
    cmdclass=cmdclass
)
