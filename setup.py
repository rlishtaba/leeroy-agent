#!/usr/bin/env python
import sys

from setuptools import find_packages
from setuptools import setup

import versioneer

if sys.version_info < (3, 5, 0):
    raise RuntimeError("Leeroy Agent requires Python 3.5.0+")

setup(
    name="leeroy-agent",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Roman Lishtaba",
    author_email="roman.lishtaba@ncr.com",
    keywords=["leeroy", "leeroy-agent", "automation"],
    description="",
    long_description="",
    url="http://www.leeroy.us",
    license="GPL v3",
    scripts=['bin/leeroy-agent-cli'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
    install_requires=[
        'packaging>=16',
        'pysocks>=1,<2',
        'PyYAML>=3,<4',
        'six>=1,<2',
        'oslash>=0,<1'
    ],
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
)
