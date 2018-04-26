# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='compareimages',
    version='0.1.0',
    description='python modules to compare images in various ways',
    long_description=readme,
    author='Richard Armstrong',
    author_email='armstrong.richard@gmail.com',
    url='https://github.com/richDsInterview/compareimages',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

