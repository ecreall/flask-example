#!/usr/bin/env python
try:
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError:
    from pip.req import parse_requirements
    from pip.download import PipSession

from setuptools import setup, find_packages


def parse_reqs(*req_files):
    """returns a list of requirements from a list of req files"""
    requirements = set()
    session = PipSession()
    for req_file in req_files:
        # parse_requirements() returns generator of pip.req.InstallRequirement objects
        parsed = parse_requirements(req_file, session=session)
        requirements.update({str(ir.req) for ir in parsed})

    return list(requirements)


setup(
    name='hellobluenove',
    version='2.0.0',
    description='Simple flask app',
    author='Bluenove',
    author_email='',
    url='https://github.com/bluenove/flask-example',
    packages=find_packages(),
    zip_safe=False,
    setup_requires=['pip>=18'],
    install_requires=parse_reqs('requirements.txt'),
)
