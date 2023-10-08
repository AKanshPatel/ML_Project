from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''This function will return the list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='ML_Project',
    version='0.0.1',
    author='Akansh',
    author_email='akanshpatel425@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    # Add a long_description if needed
    long_description='A machine learning project.',
    # Add a license if needed
    license='MIT',
)
