#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="univariate_linear_regression",
      version="0.1.0",
      description="Univariate linear regression of housing price against housing area",
      author="Dibya Chakravorty",
      packages=find_packages("src"),
      package_dir={"": "src"},
      author_email="ptcloudtech@gmail.com",
      install_requires=["jupyter==1.0.0",
                        "matplotlib==3.5.1",
                        "numpy==1.21.5",
                        "pytest==7.1.1",
                        "pytest-mpl==0.16",
                        "pytest-mock==3.10.0",
                        "scipy==1.7.3",
                        ],
      )