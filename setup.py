import os
from setuptools import setup, find_packages


__path__ = os.path.split(__file__)[0]
PACKAGE_NAME = 'odintools'


def long_description():
    return open(os.path.join(__path__, 'README.md')).read()


def version():
    build = os.environ.get('BUILD_NUMBER')
    if build == None:
        raise Exception('BUILD_NUMBER is not defined')
    return '0.1.{0}'.format(build)


setup(
    name=PACKAGE_NAME,
    author='Dmitriy Fontanov',
    author_email='ap-dc-team@odin.com',
    description='Odin setuptools extensions',
    long_description=long_description(),
    url='https://git.sw.ru/projects/DC/repos/odintools',
    version=version(),
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords=['setup', 'distutils'],
    packages=find_packages(),
    install_requires=[
        'devpi', 'markdown'
    ],
    entry_points={
        'distutils.setup_keywords': [
            'odintools = odintools.args:odintools',
            'version_getter = odintools.args:version_getter',
        ]
    }
)
