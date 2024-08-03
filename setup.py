from setuptools import setup, find_packages # type: ignore
from pathenv import version

setup(
    name='pathenv',
    version=version,
    packages=find_packages(),
    install_requires=[],
    author='foxypiratecove37350',
    author_email='foxypiratecovefnaf12@gmail.com',
    description='One of the best Python package to manipulate the `PATH` environment variable',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/foxypiratecove37350/pathenv',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
    ],
    license='GPL-2.0',
)