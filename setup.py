from setuptools import setup, find_packages

setup(
    name='arxiv-downloader',
    version='0.1.dev1',
    author='solar0037',
    author_email='solar0037@gmail.com',
    url='https://github.com/solar0037/arxiv-downloader',
    description='Package to download papers on arxiv.org.',
    packages=find_packages(),
    install_requires=[
        'bs4',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'arxiv-downloader=arxiv_downloader.cli:main'
        ]
    }
)
