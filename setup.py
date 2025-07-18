#!/usr/bin/env python3
"""
mdepub - Professional Markdown to EPUB Pipeline
Part of the ucli-tools ecosystem
"""

import setuptools
import os

# Read README for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setuptools.setup(
    name="mdepub",
    version="0.2.0",
    author="ucli-tools",
    author_email="contact@ucli-tools.org",
    description="A professional tool to convert Markdown files to EPUB format.",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ucli-tools/mdepub",
    project_urls={
        "Bug Tracker": "https://github.com/ucli-tools/mdepub/issues",
        "Documentation": "https://github.com/ucli-tools/mdepub/tree/main/docs",
        "Source Code": "https://github.com/ucli-tools/mdepub",
        "ucli-tools": "https://github.com/ucli-tools",
    },
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Text Processing :: Markup",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'mdepub=mdepub.cli:main',
        ],
    },
    keywords=[
        "epub",
        "markdown",
        "converter",
        "ucli-tools",
        "publishing"
    ],
)
