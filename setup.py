from setuptools import setup, find_packages

setup(
    name='arxiv-downloader',
    version='0.1-dev',
    packages=find_packages(),
    install_requires=[
        'bs4'
    ],
    entry_points={
        'console_scripts': [
            'arxiv-downloader=arxiv_downloader.cli:main'
        ]
    }
)
