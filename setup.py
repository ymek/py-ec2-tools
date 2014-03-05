#!/usr/bin/env python

__version__ = '0.0.1'

from setuptools import setup
from setuptools import find_packages

setup(
    name='py-ec2-tools',
    version=__version__,
    author='Myke Stubbs',
    author_email='myke@bittorrent.com',
    description='A collection of tools for managing EC2 clusters',
    url='http://github.com/ymek/py-ec2-tools',
    license='RESERVED',
    packages=find_packages()
)
