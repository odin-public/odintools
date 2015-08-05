import os
from setuptools import setup, find_packages


PACKAGE_NAME = 'odintools'

long_description = open(os.path.join(os.getcwd(), 'README.md')).read()


setup(
    name=PACKAGE_NAME,
    author='Dmitriy Fontanov',
    author_email='ap-dc-team@odin.com',
    description='Odin setuptools extensions',
    long_description=long_description,
    url='https://git.sw.ru/projects/DC/repos/odintools',
    version='0.1.5',
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
