"""
This setup.py script is based on examples from  
https://pythonhosted.org/an_example_pypi_project/setuptools.html
https://docs.python.org/3/distutils/setupscript.
https://github.com/pypa/sampleproject/blob/master/setup.py
"""
from setuptools import setup, find_packages

with open('README.txt', 'r') as fh: 
    long_description = fh.read()

# noinspection PyPackageRequirements
setup(
    name = 'potions',
    version = '0.1.0',
    packages = find_packages(),
    author = 'ASPP 2021',
    author_email = 's.snape@hogwarts.ac.uk',
    description = 'an example python package',
    long_description = long_description,
    license = 'MIT',
    url = 'https://github.com/ASPP/2021-bordeaux-ODD.git',
    install_requires = ['numpy >= 1.14.0',
                        'matplotlib >= 3.0.0',
                        'pytest >= 3.0.0'],
)

