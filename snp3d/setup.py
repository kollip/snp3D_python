# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py
import os, sys
from setuptools import setup, find_packages

def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

    
setup(
    name='snp3d',
    version='0.0.1',
    description='Module for reading snp3D files in Python',
    long_description=readme,
    author='Yusuke Koroyasu',
    author_email='koroyasu.st@gmail.com',
    url='https://github.com/kollip/snp3D_python',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=read_requirements()
)
