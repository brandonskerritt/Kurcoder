#!/usr/bin/env python3
'''
setup.py

    Installs Kurcoder as a CLI appliation locally

'''

import os
import setuptools

NAME = "kurcoder"
VERSION = "0.0.1"

REPO = "https://github.com/0xkurome/Kurcoder"
DESC = "Simple encoder & decoder tool"

# main
setuptools.setup(
        name = NAME,
        version = VERSION,
        author = '0xkurome',
        description = DESC,
        license = 'MIT'
        url = REPO,
        package_dir={'': 'src'},
        install_requires=[
            "ipcalc",
        ],
        classifiers=[
            "Development Status :: 1 - Planning",
            "Intended Audience :: End Users/Desktop",
            "Environment :: Console",
            "Natural Language :: English",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
        ]
)
