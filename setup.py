#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# dockerinfo - Docker container information extractor 


from setuptools import setup
import io
from os import path


here = path.abspath(path.dirname(__file__))

with io.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="dockerinfo",
    version="0.1",
    description="Docker container information extractor",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/croketillo/dockerinfo',
    author="croketillo",
    author_email="croketillo@gmail.com",
    license='GNU-3',
    keywords=['docker', 'docker info', 'container'],
    packages=["dockerinfo"],
    install_requires=['docker'],
    
)
