# coding: utf-8

"""
    DSM Common Api wrapper

"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "mipt-api-wrapper"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["aiohttp", "mipt-auth-wrapper==1.0.0"]

setup(
    name=NAME,
    version=VERSION,
    description="Wrapper functions to add tokens",
    author="Vasily Baydin",
    author_email="vasyafon@gmail.com",
    url="",
    keywords=["DSM Common Auth"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description="""\
    """
)
