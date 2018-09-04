#!/usr/bin/env python3
from setuptools import setup

setup(
    name="tap-greenhouse",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Simon Data",
    url="http://simondata.com",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_greenhouse"],
    install_requires=[
        "singer-python>=5.0.12",
        'requests==2.18.4',
        "pendulum==1.2.0",
    ],
    entry_points="""
    [console_scripts]
    tap-greenhouse=tap_greenhouse:main
    tap-greenhouse-class=tap_greenhouse.class_invoke:class_main
    """,
    packages=["tap_greenhouse"],
    include_package_data=True,
)
