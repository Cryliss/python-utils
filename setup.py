#!usr/bin/env python

from setuptools import setup, find_packages

setup(name="pyutils",
      version="0.1",
      description="Test for pip install git+",
      url="https://github.com/Cryliss/python-utils.git",
      install_requires=["numpy", "opencv-python", "Pillow"],
      packages=find_packages()
)
