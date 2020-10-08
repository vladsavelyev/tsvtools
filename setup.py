#!/usr/bin/env python
from setuptools import setup

pkg = 'tsvtools'

try:
    import versionpy
except ImportError:
    res = input('Installation requires versionpy. Install it now? [Y/n]')
    if res.lower().startswith('n'):
        raise
    os.system('pip install versionpy')
    import versionpy

version = versionpy.get_version(pkg)

setup(
    name=pkg,
    version=version,
    author='Vlad Saveliev',
    author_email='vladislav.sav@gmail.com',
    description='Utilities for operating with tab-separated files: viewing, filtering, reordering',
    keywords='bioinformatics',
    url='https://github.com/vladsaveliev/' + pkg,
    license='GPLv3',
    packages=[pkg],
    include_package_data=True,
    zip_safe=False,
    install_requires=['click', 'versionpy'],
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
