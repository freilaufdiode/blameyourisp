#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
setup(
    name='blameyourisp',
    version='0.2',
    author='freilaufdiode',
    url='https://github.com/freilaufdiode/blameyourisp',
    packages=['blameyourisp_graph', 'blameyourisp'],
    entry_points={
        'console_scripts': [
            'blameyourisp-graph=blameyourisp_graph.blameyourisp_graph:main',
            'blameyourisp=blameyourisp.blameyourisp:main'
        ]
    },
    install_requires=[
        'matplotlib',
        'python-dateutil',
        'speedtest-cli'],
    license="Apache 2.0"
)

