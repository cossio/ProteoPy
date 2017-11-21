from setuptools import setup


setup(name='ProteoPy', version='0.1.0',
       url='https://github.com/cossio/ProteoPy',
       license='MIT',
       author='Jorge Fernandez-de-Cossio-Diaz',
       author_email='j.cossio.diaz@gmail.com',
       description='Tools to handle proteomics data.',
       packages=['ProteoPy'],
       scripts=['bin/go.py', 'bin/compartments.py', 'bin/uniprot.py'],
       long_description=open('README.md').read(),
       zip_safe=False,
       setup_requires=['bioservices', 'mygene'],
       test_suite='nose.collector',
       tests_require=['nose'],
       include_package_data=True)