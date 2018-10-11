#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='hellobluenove',
    version='1.1',
    description='Simple flask app',
    author='Bluenove',
    author_email='',
    url='https://github.com/bluenove/flask-example',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'flask'
    ]
)