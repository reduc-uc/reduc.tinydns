from setuptools import setup, find_packages
import os

version = open('version.txt').readline().strip()

long_description = (
    open("README.rst").read()
    + '\n' +
    open(os.path.join("docs", "HISTORY.rst")).read()
    + '\n')

setup(name='reduc.tinydns',
      version=version,
      description="DJB's tinydns utility for generating a zone file from multiple sources",
      long_description=long_description,
      classifiers=[
      ],
      keywords='',
      author='Jose Dinuncio',
      author_email='jose.dinuncio@gmail.com',
      url='https://github.com/reduc-uc/reduc.tinydns',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['reduc', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      extras_require={
          'test': [
          ]
      },
      entry_points="""
      """,
      )