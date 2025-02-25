from setuptools import find_packages, setup
from typing import List

HYPEN_E = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function returns a list of requirements
    '''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
            
    if HYPEN_E in requirements:
                requirements.remove(HYPEN_E)
    return requirements
    

setup(
    name='Crime LA Forecast',
    version="0.1.0",
    packages=find_packages(),
    author="Arav Pandey",
    author_email="aravpandey3010@gmail.com",
    install_requires=get_requirements('requirements.txt'),
)