import ez_setup
ez_setup.use_setuptools()

import setuptools
import os

# Use app's version
import metax

# Use the readme as the long description baked into the application itself
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(name="MetaXcan",
                 version=metax.__version__,
                 author="Alvaro Barbeira, Eric Torstenson",
                 author_email='alvarobarbeira@gmail.com, eric.s.torstenson@vanderbilt.edu',
                 url="TBD",
                 packages=['metax','tests','metax.gwas','metax.metaxcan', 'metax.deprecated'],
                 license="TBD",
                 scripts=[  'M00_prerequisites.py',
                            'M01_covariances_correlations.py',
                            'M02_variances.py',
                            'M03_betas.py',
                            'M04_zscores.py',
                            'MetaXcan.py',
                            'MetaXcanUI.py',
                            'MetaMany.py'],
                 description=["TBD"],
                 install_requires=['scipy>=1.2.2', 'numpy>=1.14.2', 'pandas>=0.22.0', 'mock>=2.0.0', 'patsy>=0.5.0', 'statsmodels>=0.10.0', 'h5py>=2.7.1', 'h5py-cache>=1.0'],
                 long_description=read('Readme.md'),
                 keywords=['TBD'],
                 test_suite='tests',
                 package_data={'tests/files':['*']},
                 classifiers=[
                    "Development Status :: 4 - Beta",
                    "Topic :: Utilities",
                    "Topic :: Scientific/Engineering :: Bio-Informatics",
                    "Topic :: Software Development :: Libraries",
                    "Programming Language :: Python :: 2.7"
                 ],
)
