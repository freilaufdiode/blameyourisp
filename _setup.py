#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
setup(
    name='blameyourisp-graph',
    version='0.1',
    packages=['blameyourisp_graph'],
    entry_points={
        'console_scripts': [
            'blameyourisp-graph=blameyourisp_graph.blameyourisp_graph:main'
        ]
    }
)

