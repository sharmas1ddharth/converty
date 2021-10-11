from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'converty package testing'
LONG_DESCRIPTION = 'A python package that can convert any file type to any type'

# Setting up
setup(
    name="converty",
    version=VERSION,
    author="Siddharth Sharma",
    author_email="ssiddharth408@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pillow'], # add any additional packages that
)
