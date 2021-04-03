import sys

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyPS4Controller",
    version="1.2.5",
    author="Artur Spirin",
    author_email="as.no.replies@gmail.com",
    description="Simple hooks for PS4 controller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArturSpirin/pyPS4Controller",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ],
    keywords=["playstation", "ps4", "controller", "binding", "hooks"],
    entry_points={
          'console_scripts': [
              'py2ps4c = pyPS4Controller.__main__:main'
              if sys.version_info[0] < 3 else
              'py3ps4c = pyPS4Controller.__main__:main',
          ]
    },
)
