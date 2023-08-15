from setuptools import find_packages, setup     
 #find_packages is used for finding packages easily

from typing import List
HYPEN_E_DOT = '-e .'

#it is used for installing whatever the packages or libraries required for the project.
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
name='ML Project end to end',
version='0.0.1',
author='Pratham',
author_email='prathamesh11psd@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)