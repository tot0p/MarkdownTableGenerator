#-*- coding: utf-8 -*-

import MDTable
import setuptools
from setuptools import setup


setup(
    name='MDTable',
    version=MDTable.__version__,
    description=MDTable.__doc__,
    author="tot0p",
    author_email="thomas.lemaitre.78420@gmail.com",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tot0p/MarkdownTableGenerator",
    license="MIT",
    packages=setuptools.find_packages(),
)

