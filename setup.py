from setuptools import setup
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ecoledirect',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='3.5.1',
    description='With this package you can get the data from the website www.ecoledirect.com.',
    url='https://github.com/Snowy-27/EcoleDirect',
    author='Dan Habib',
    author_email='dan.habib@yahoo.fr',
    license='unlicense',
    packages=['ecoledirect'],
    zip_safe=False
)
