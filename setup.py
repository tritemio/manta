from setuptools import setup
import versioneer

project_name = 'manta'

## Configure versioneer
versioneer.VCS = 'git'
versioneer.versionfile_source = project_name + '/_version.py'
versioneer.versionfile_build = project_name + '/_version.py'
versioneer.tag_prefix = '' # tags are like 1.2.0
versioneer.parentdir_prefix = project_name + '-'


## Metadata
long_description = """
manta
=====

Utilities for the Manta SPAD array from POLIMI.
"""

setup(name = project_name,
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      author = 'Antonino Ingargiola',
      author_email = 'tritemio@gmail.com',
      url          = 'http://github.com/tritemio/phconvert/',
      download_url = 'http://github.com/tritemio/phconvert/',
      install_requires = ['numpy'],
      license = 'GPLv2',
      description = ("Utilities for the Manta SPAD array from POLIMI."),
      long_description = long_description,
      platforms = ('Windows', 'Linux', 'Mac OS X'),
      classifiers=['Intended Audience :: Science/Research',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Scientific/Engineering',
                   ],
      packages = ['manta'],
      keywords = ('SPAD-array single-photon SPAD confocal'),
      )

