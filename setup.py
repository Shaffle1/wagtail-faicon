#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="wagtail-faicon",
    version="0.1.1",
    author="Paul Woods",
    author_email="shaffle8@yandex.ru",
    description="Django Wagtail Font Awesome 5 icon picker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shaffle1/wagtail-faicon",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Framework :: Django :: 2.1',
    ],
    install_requires=[
        'PyYAML',
        'Django>=2.1'
    ],
)
