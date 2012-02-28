#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages

setup(name="lastpy",
      version="0.1",
      description="Last.FM library for python",
      license="Apache v2.0",
      author="Martin Chorley",
      author_email="martin@martinjc.com",
      url="http://github.com/martinjc/laspy",
      packages = find_packages(),
      keywords= "last.fm library",
      zip_safe = True)