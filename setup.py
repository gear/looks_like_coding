#!/usr/bin/env python


"""
Setup script for looks_like_coding
"""


import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as f:
    readme_content = f.read().strip()


version = None
author = "HNT"
email = "hoangnt@me.com"
source = None
with open(os.path.join("looks_like_coding", "__init__.py")) as f:
    for line in f:
        if line.strip().startswith("__version__"):
            version = line.split('=')[1].strip().replace('"', '').replace("'", '')
        else:
            break


setup(
    name="looks_like_coding",
    author=author
    author_email=email
)
