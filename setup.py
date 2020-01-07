from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.1'
HERE = Path(__file__).parent
README = (HERE / 'README.md').read_text()

setup(
    name='stampy',
    version=VERSION,
    description='Commandline tool for quickly entering multiple similar commands.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/voidcase/stampy',
    py_modules='stampy',
    entry_points={
            'console_scripts': [
                'stampy=stampy.stam:run'
            ]
        }
    )
