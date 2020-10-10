import setuptools

from chpass import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chpass",
    version=__version__,
    author="Ben Gabay",
    author_email="ben.gabay38@gmail.com",
    license="License :: OSI Approved :: MIT License",
    description="export and import chrome passwords",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bengabay11/chpass",
    packages=setuptools.find_packages(),
    install_requires=[
        "sqlalchemy==1.3.18",
        "pandas==1.1.2"
    ],
    entry_points={
        'console_scripts': ['chpass = chpass.__init__:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
