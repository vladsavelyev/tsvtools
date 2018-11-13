#!/usr/bin/env python
from setuptools import setup
import release

import tsvtools
package_name = tsvtools.__name__

version = release.get_version(package_name)

setup(
    name=package_name,
    version=version,
    author='Vlad Saveliev',
    author_email='vladislav.sav@gmail.com',
    description='Utilities for operating with tab-separated files: viewing, filtering, reordering',
    keywords='bioinformatics',
    url='https://github.com/vladsaveliev/' + package_name,
    license='GPLv3',
    packages=[package_name],
    include_package_data=True,
    zip_safe=False,
    install_requires=release.get_reqs(),
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
