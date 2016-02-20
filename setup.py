from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup
from glob import glob


__version__ = '0.1b0'


setup(
    name='babygdcli',
    version=__version__,
    description='little PyDrive CLI',
    py_modules=[
        'babygdcli',
    ],
    scripts=glob('scripts/*'),
    install_requires=[
        'PyDrive>=1.0.0',
    ],
    url='https://github.com/cjmay/babygdcli',
    license='BSD',
)