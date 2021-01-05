#!/usr/bin/env python
from setuptools import setup

pkg = 'tsvtools'

setup(
    name=pkg,
    version='0.1.0',
    author='Vlad Savelyev',
    author_email='vladislav.sav@gmail.com',
    description='Utilities for operating with tab-separated files: viewing, filtering, reordering',
    keywords=['bioinformatics', 'data science'],
    url='https://github.com/vladsaveliev/' + pkg,
    license='GPLv3',
    packages=[pkg],
    include_package_data=True,
    zip_safe=False,
    scripts=['scripts/tsvtools', 'scripts/tsv', 'scripts/cols'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
    ],
)
