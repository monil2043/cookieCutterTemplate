#!/usr/bin/env python
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

setup(
    name='{{cookiecutter.service_name}}-cdk',
    version='1.0',
    description='CDK code for deploying the serverless service',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.12',
    ],
    url='https://github.com/ContactCenterOnAWS/{{cookiecutter.repo_name}}',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email}}',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    package_data={'': ['*.json']},
    include_package_data=True,
    python_requires='>=3.12',
    install_requires=[],
)
