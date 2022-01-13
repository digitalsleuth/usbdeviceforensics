#!/usr/bin/env python3
from setuptools import setup, find_packages

with open("README.md", encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name="usbdeviceforensics",
    version="1.0.0",
    author="Mark Woan, Corey Forman",
    url="https://github.com/digitalsleuth/usbdeviceforensics",
    description=("Python3 tool for extracting USB information from Windows Registry hives"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "python-registry"
    ],
    entry_points={
        'console_scripts': [
            'usbdeviceforensics = usbdeviceforensics.usbdeviceforensics:main'
        ]
    },
    package_data={'': ['README.md']}
)
