from setuptools import setup

setup(
    name='filesize',
    version='1.0',
    description='A tool for checking file sizes',
    author='Your Name',
    author_email='rupesh4321@gmail.com',
    url='https://github.com/rupesh43210/filesize',
    packages=['filesize'],
    install_requires=[
        'tabulate',
        'termcolor',
    ],
    entry_points={
        'console_scripts': [
            'filesize = filesize.file_size:main',
        ],
    },
)
