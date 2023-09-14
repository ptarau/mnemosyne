from setuptools import setup
import setuptools

import mnemosyne

with open('requirements.txt') as f:
    required = f.read().splitlines()
with open("README.md", "r") as f:
    long_description = f.read()

version = mnemosyne.__version__
setup(name='mnemosyne',
      version=version,
      description='Deep, recursive, goal-driven LLM explorer',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/ptarau/mnemosyne.git',
      author='Paul Tarau',
      author_email='paul.tarau@gmail.com',
      license='GPL-3',
      packages=setuptools.find_packages(),
      package_data={
          'mnemosyne': [
            *.jpg
          ]
      },
      include_package_data=True,
      install_requires=required,
      zip_safe=False
      )
