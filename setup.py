import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="mdepub",
    version="0.1.0",
    author="ucli-tools",
    description="A tool to convert Markdown files to EPUB format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ucli-tools/mdepub",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'mdepub=mdepub.cli:main',
        ],
    },
)
