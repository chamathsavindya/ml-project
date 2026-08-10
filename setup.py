from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_reqirements(file_path:str)->List[str]:
    """this function will return list of requirements"""
    reqirements = []
    with open(file_path) as file_obj:
        reqirements = file_obj.readlines()
        reqirements = [reqirement.replace("\n","") for reqirement in reqirements] 

    if HYPEN_E_DOT in reqirements:
        reqirements.remove(HYPEN_E_DOT) 

    return reqirements

setup(

    name = "mlproject",
    version = "0.0.1",
    author = "chamathsavindya",
    packages=find_packages(),
    install_requires = get_reqirements("requirements.txt")
)