from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.1.1'
HERE = Path(__file__).parent
README = (HERE / 'README.md').read_text()

setup(
    name='stampel',
    version=VERSION,
    description='Commandline tool for quickly entering multiple similar commands.',
    long_description=README,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/voidcase/stampel',
    download_url='https://github.com/voidcase/stampel/archive/v{}.tar.gz'.format(VERSION),
    py_modules=['stampel'],
    packages=find_packages(),
    keywords=['data-entry', 'utility', 'commandline'],
    entry_points={
            'console_scripts': [
                'stampel=stampel.stampel:run'
            ]
        },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Topic :: Utilities',
        ],
    )
