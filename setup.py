#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'generalutils']

setup(
    author="Tomek Joostens",
    author_email='joostenstomek@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    description="Program to ease picture development flow ",
    entry_points={
        'console_scripts': [
            'picturebot=picturebot.cli:main',
            'pb=picturebot.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='picturebot',
    name='picturebot',
    packages=find_packages(include=['picturebot']),
    setup_requires=requirements,
    test_suite='tests',
    tests_require=requirements,
    url='https://github.com/Tomekske/picturebot',
    version='0.0.18',
    zip_safe=False,
)
