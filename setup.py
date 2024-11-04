# Resonsible to create my ML application as a py
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    ''' return list of requirments.'''
    requirements = []
    with open(file_path)as file_obj:
        requirements =file_obj.readline()
        [req.replace('\n','')for req in requirements  ]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name = 'Wireless_Mob_vaccum_Project',
    version= '0.0.1',
    author= 'Biovr Arjayal',
    author_email='bivorbivor@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)