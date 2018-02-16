# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Nephila',
    version='0.1.0',
    description='Cosmic Web Classifier',
    long_description=readme,
    author='Sebastian Bustamnate',
    author_email='sebastian.bustamante@h-its.org',
    url='https://github.com/sbustamante',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

