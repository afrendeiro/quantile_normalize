#! /usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='quantile_normalize',
    packages=['quantile_normalize'],
    description='Quantile normalization of masked numpy arrays per Bolstad et. al',
    author='Andrew Yates',
    url='https://github.com/andrewdyates/quantile_normalize',
    dependencies=['numpy, scipy']
)
