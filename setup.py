import os
from setuptools import setup, find_packages


__path__ = os.path.split(__file__)[0]
PACKAGE_NAME = 'odintools'


def long_description():
    return open(os.path.join(__path__, 'README.md')).read()


def version():
    with open(os.path.join(__path__, 'version.txt'), 'r') as verfile:
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
    author='Odin Automation DevCloud team',
    author_email='support@odin.com',
    description='Odin setuptools extensions',
    long_description=long_description(),
    url='http://odin.com',
    version=version(),
    license='Other/Proprietary License',
    classifiers=[
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords=['setup', 'distutils'],
    packages=find_packages(),
    install_requires=[
        'importlib',  # note: importlib is a missing depend of markdown
        'markdown==2.6.2',
    ],
    entry_points={
        'distutils.setup_keywords': [
            'odintools = odintools.args:odintools',
            'version_getter = odintools.args:version_getter',
        ]
    },
    cmdclass=cmdclass
)
