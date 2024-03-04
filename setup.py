"""A simple method to compress a copy of a directory for Python 3.5+

See:
https://github.com/landoskape/freezedry
"""

from setuptools import setup

description = "A spec-compliant gitignore parser for Python 3.5+"
setup(
    name="gitignore_parser",
    version="0.0.1",
    author="Andrew Landau",
    author_email="andrew+tyler+landau+getridofthisanddtheplusses@gmail.com",
    description=description,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords=["python code", "compression", "compress"],
    url="https://github.com/landoskape/freezedry",
    py_modules=["freezedry"],
    license="MIT",
    install_requires=["gitignore_parser"],
)
