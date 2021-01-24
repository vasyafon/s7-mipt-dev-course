# coding: utf-8

"""
    DSM Common Auth

"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "mipt-auth-wrapper"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["authlib", "pydantic", "auth-aiohttp-client==1.0.0", "flask", "itsdangerous", "pytz"]

setup(
    name=NAME,
    version=VERSION,
    description="Auth procedures to decode access tokens",
    author="Vasily Baydin",
    author_email="vasyafon@gmail.com",
    url="",
    keywords=["Auth"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description="""\
    """
)
