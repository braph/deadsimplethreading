#!/usr/bin/python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deadsimplethreading",
    version="0.0.1",
    author="Benjamin Abendroth",
    author_email="braph93@gmx.de",
    description="dead simple threading",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/braph/deadsimplethreading",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
