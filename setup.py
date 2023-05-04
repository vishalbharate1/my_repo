from setuptools import find_packages, setup
from typing import List

Requirement_File_Name='requirements.txt'
REMOVE_PACKAGE='-e .'

def get_requirements()->List[str]:
    pass


setup(
    name='SMS',
    version='0.0.1',
    description= 'Indutry ready SMS Spam Project',
    author= 'Vishal Bharate',
    author_email= 'vishalbharate@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements()
    )

def get_requirements()->List[str]:
    with open (Requirement_File_Name) as requirment_file:
        requirement_list=requirment_file.readline()
    requirement_list=[requirement_name.replace('\n','') for requirement_name in requirement_list]

    if REMOVE_PACKAGE in requirement_list:
        requirement_list.remove(REMOVE_PACKAGE)
    return requirement_list
    
