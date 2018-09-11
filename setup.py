"""Setup file to Not Another Neuroimaging Slicer

"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nanslice',
    version='1.0.0',
    description='Scripts to slice and display neuroimages (probably stored in nifti format)',
    url='https://github.com/spinicist/nanslice',
    author='Tobias Wood',
    author_email='tobias.wood@kcl.ac.uk',
    license='MPL',
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Neuroimagers',
                 'Topic :: Scientific/Engineering :: Visualization',
                 'License :: OSI Approved :: Mozilla Public License',
                 'Programming Language :: Python :: 3',
    ],
    keywords='neuroimaging nifti',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nanslicer=nanslice.nanslicer:main',
            'nanviewer=nanslice.nanviewer:main',
            'nanscroll=nanslice.nanscroll:main'
        ],
    },
)