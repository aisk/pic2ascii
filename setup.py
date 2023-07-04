from os import path
from setuptools import setup, find_packages


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='pic2ascii',
    version='0.1.0',

    description='A simple tool to draw yout image to ascii code',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/aisk/pic2ascii',
    author='asaka',
    author_email='aisk1988@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.5',
    ],

    keywords='image to ascii',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'pillow>=8,<11',
        'fire~=0.3',
    ],
)
