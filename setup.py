from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(filepath:str) -> List[str]:

    '''
    this function will return the list of requirements
    '''
    requirements = []
    try:
        with open(filepath, "r") as file:
            for line in file:
                # Strip whitespace and skip comments or empty lines
                line = line.strip()
                if line and not line.startswith("#"):
                    requirements.append(line)
                
                if HYPEN_E_DOT in requirements:
                    requirements.remove(HYPEN_E_DOT)


    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    return requirements

setup(

name = "Machine-Learning-Project",
version= '0.0.1',
author= 'AnujaP',
author_email= 'anuja.parab4@gmail.com',
packages= find_packages(),
install_requires=get_requirements('requirements.txt')

)