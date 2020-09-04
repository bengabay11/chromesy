import setuptools

from chromesy import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chromesy",
    version=__version__,
    author="Ben Gabay",
    author_email="ben.gabay38@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bengabay11/chromesy",
    packages=setuptools.find_packages(),
    install_requires=[
        "sqlalchemy==1.3.18"
    ],
    entry_points={
        'console_scripts': ['chromesy = chromesy.cli:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)