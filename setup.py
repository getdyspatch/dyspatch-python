# coding: utf-8

"""
    Dyspatch API

    # Introduction
    The Dyspatch API is based on the REST paradigm and features resource based
    URLs with standard HTTP response codes to indicate errors.
    We use standard HTTP authentication and request verbs and all responses are
    JSON formatted. See our [Implementation
    Guide](https://docs.dyspatch.io/development/implementing_dyspatch/) for
    more details on how to implement Dyspatch.

    OpenAPI spec version: 2019.10
    Contact: support@dyspatch.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "dyspatch-python"
VERSION = "3.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]

with open("README.md") as fp:
    long_description = fp.read()

setup(
    name=NAME,
    version=VERSION,
    description="Dyspatch API Client",
    author_email="support@dyspatch.io",
    url="https://github.com/getdyspatch/dyspatch-python",
    keywords=["Swagger", "Dyspatch API", "OpenAPI"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
)
