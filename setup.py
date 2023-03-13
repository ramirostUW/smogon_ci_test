from typing import List

from setuptools import setup, find_packages
from pathlib import Path


def get_install_requires() -> List[str]:
    """Returns requirements.txt parsed to a list"""
    fname = Path(__file__).parent / 'requirements.txt'
    targets = []
    if fname.exists():
        with open(fname, 'r') as f:
            targets = f.read().splitlines()
    return targets


setup(
   name='smogonapi',
   version='1.0',
   description='A module that provides API to query Pokemon information backed by Smogon webpage',
   author='UW DATA515 group',
   author_email='foomail@foo.example',
   packages=find_packages(),
   install_requires=get_install_requires(),
   package_data={'': ['*.csv']},
   include_package_data=True,
   scripts=['bin/start_smogon_api_local_server']
)