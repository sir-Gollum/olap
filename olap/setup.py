#-*- coding:utf-8 -*-

from setuptools import setup

setup(name='olap',
    version='0.1',
    description='Interface to OLAP DBs',
    author='Norman Krämer',
    author_email='kraemer.norman@googlemail.com',
    packages=['olap'],
    namespace_packages=['olap'],
    package_dir={'olap': 'olap'},
    install_requires=[
      'zope.interface == 3.6.7',
      'zope.schema == 4.1.1',
    ],
    url="https://github.com/may-day/olap",
    license='Apache Software License 2.0',
    classifiers = [
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules"
        ]
)
