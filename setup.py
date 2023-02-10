from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="aws-sso-wrangler",
    description="A tiny tool for controlling many AWS SSO profiles",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Jakub Synowiec",
    url="https://github.com/jsynowiec/aws-sso-wrangler",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["aws_sso_wrangler"],
    entry_points="""
        [console_scripts]
        aws-sso-wrangler=aws_sso_wrangler.cli:cli
    """,
    install_requires=["inquirer"],
    python_requires=">=3.7",
)
