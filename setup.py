import setuptools
from setuptools import version

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsoninput",
    version="0.0.1",
    author="Riley Hall",
    author_email="riley.hall.va@gmail.com",
    description="A utility for loading and checking JSON files against a schema",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rileychall/json-input",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
