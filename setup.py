from setuptools import setup

setup(
    name='bibidy',
    version='0.0.1',
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'bibidy=bibidy:bibidy'
        ]
    }
)