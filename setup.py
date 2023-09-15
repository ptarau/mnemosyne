from setuptools import setup
import setuptools

import memesis

with open('requirements.txt') as f:
    required = f.read().splitlines()
with open("README.md", "r") as f:
    long_description = f.read()

version = memesis.__version__
setup(name='memesis',
      version=version,
      description="Custodian and live editor of your LLM's memory",
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/ptarau/mnemosyne.git',
      author='Paul Tarau',
      author_email='ptarau@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      package_data={
          'memesis': [
            '*.jpg'
          ]
      },
      include_package_data=True,
      install_requires=required,
      zip_safe=False
      )
