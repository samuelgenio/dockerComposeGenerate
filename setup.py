from setuptools import setup, find_packages

setup(
    name='Generate Compose',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'Click', 'setuptools'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'generate = generate:cli',
        ],
    },
)
