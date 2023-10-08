from setuptools import setup, find_packages

setup(
    name='bibidy',
    version='0.0.1',
    install_requires=[
        'Click',
        'pyptex',
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'bibidy=bibidy.bibidy:bibidy'
        ]
    }
)