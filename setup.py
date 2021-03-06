from setuptools import setup
from glob import glob


__version__ = '0.2b11'


setup(
    name='babygdcli',
    version=__version__,
    description='little Google Drive CLI',
    py_modules=[
        'babygdcli',
    ],
    scripts=glob('scripts/*'),
    install_requires=[
        'google-api-python-client>=1.6.2',
        'oauth2client',
    ],
    url='https://github.com/cjmay/babygdcli',
    license='BSD',
)
