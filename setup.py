#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


package_name = 'robot-detect'

readme = """
robot-detect
============

Tool to detect the ROBOT vulnerability (Return of Bleichenbacher's Oracle Threat).

More Info:

https://robotattack.org/
"""

VERSION = 0.1

setup(
    name=package_name,
    version=VERSION,
    description="Detection for ROBOT vulnerability",
    long_description=readme,
    author="Hanno Böck, Juraj Somorovsky, Craig Young",
    author_email='hanno@hboeck.de',
    url='https://www.robotattack.org',
    packages=[],
    scripts=['robot-detect'],
    install_requires=[
        'gmpy2',
        'cryptography'
    ],
    license="CC0",
    zip_safe=True,
    keywords=('tls', 'robot', 'security', 'vulnerability'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
