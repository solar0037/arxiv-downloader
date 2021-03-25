from setuptools import setup, find_packages


setup(
    name='arxiv-downloader',
    version='0.1.dev1',
    author='Hojun Sa',
    author_email='solar0037@gmail.com',
    url='https://github.com/solar0037/arxiv-downloader.git',
    description='Package to download papers on arxiv.org.',
    project_urls={
        "Bug Tracker": "https://github.com/solar0037/arxiv-downloader/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
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
