from setuptools import setup, find_packages

setup(
    name='EskomMetrics',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url='https://github.com/AmyG01/Team-4-Project-2/EskomMetrics.git',
    author='Philani Mkhize',
    author_email='Philaninkanyiso@gmail.com'
)
