import setuptools
from distutils.core import setup

setup(name='fdcorpus',
      version='0.1.0',
      description="Female Daily Network's ",
      author='Ykäz Mihar',
      author_email='zaky@femaledaily.com',
      url='https://www.python.org/zkrhm/fdn/',
      packages=setuptools.find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      entry_points={
          'console_scripts': ['fdcorpus=fdcorpus.cmd:main'],
      })
