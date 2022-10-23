from setuptools import setup

setup(
    name='chris-codecarbon-plugin',
    version='1.0.0',
    description='A ChRIS plugin to measure the amount of carbon emissions using the tool called codecarbon',
    author='FNNDSC',
    author_email='faithkovi@gmail.com',
    url='https://github.com/FaithKovi/chris-codecarbon-plugin',
    py_modules=['codecarbon'],
    install_requires=['chris_plugin'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'codecarbon = codecarbon:main'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ],
    extras_require={
        'none': [],
        'dev': [
            'pytest~=7.1',
            'pytest-mock~=3.8'
        ]
    }
)
