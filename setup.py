'''
pip install
'''

import glob
from setuptools import setup


setup(name='ProteoPy', version='0.1.0', license='MIT',
      url='https://github.com/cossio/ProteoPy',
      author='Jorge Fernandez-de-Cossio-Diaz',
      author_email='j.cossio.diaz@gmail.com',
      description='Tools to handle proteomics data.',
      packages=['ProteoPy'],
      scripts=glob.glob("bin/*.py") + glob.glob("bin/*.sh"),
      long_description=open('README.md').read(),
      zip_safe=False,
      setup_requires=['bioservices', 'mygene', 'termcolor'],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True)
