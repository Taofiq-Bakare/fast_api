#!/usr/bin/env python

"""
The setup file.
"""

import os

from setuptools import find_packages, setup

setup(
    name="boring_python",
    version="0.0.1",
    description="A starter template for python projects",
    long_description=open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
    ).read(),
    long_description_content_type="text/markdown",
    author="Bakare Taofiq",
    packages=find_packages(),
    install_requires=[
        "setuptools",
    ],
)
