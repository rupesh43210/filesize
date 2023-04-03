from setuptools import setup

setup(
    name='file_size',
    version='0.1',
    author='Your Name',
    author_email='your.email@example.com',
    description='A package to calculate file size from any location',
    url='https://github.com/your-username/file_size',
    py_modules=['file_size', 'functions'],
    install_requires=['tabulate', 'termcolor'],
    entry_points={
        'console_scripts': [
            'filesize = file_size:main'
        ]
    }
)
