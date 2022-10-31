#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="enigma-bench-proj",
    version="0.1.0",
    author="Phillip Kamps",
    author_email="phillip.kamps@slalom.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    maintainer="Phillip Kamps",
    maintainer_email="phillip.kamps@slalom.com",
    license="GNU",
    url="",
    description="",
    long_description=read("README.md"),
    python_requires=">=3.5",
    install_requires=[
        "pytest>=7.1.2",
        "numpy>=1.23.4"
    ]
)
