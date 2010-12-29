#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import jsopo
from jsopo import version
from setuptools import setup

description = "Precompiler providing operator overloading for JavaScript."
cur_dir = os.path.dirname(__file__)
try:
    long_description = open(os.path.join(cur_dir, 'README.md')).read()
except:
    long_description = description

setup(
    name = "jsopo",
    version = version.get(),
    url = 'https://github.com/bebraw/jsopo',
    license = 'BSD',
    description = description,
    long_description = long_description,
    author = jsopo.__author__,
    author_email = 'bebraw@gmail.com',
    packages = ['jsopo', ],
    package_dir = {'jsopo': 'jsopo', },
    install_requires = ['setuptools', ],
    entry_points="""
    [console_scripts]
    jsopo = jsopo.runner:main
    """,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: JavaScript'
        'Topic :: Software Development :: Precompiler',
    ],
)
