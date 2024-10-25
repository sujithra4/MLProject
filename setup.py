from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOTS='-e.'

def get_requirements(file_path:str)->List[str]:

    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]

        if HYPEN_E_DOTS in requirements:
            requirements.remove(HYPEN_E_DOTS)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='sujithra',
    author_email='20AD38@kcgcollege.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)