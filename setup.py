from setuptools import setup, find_packages

setup(
    name='pic2ascii',
    version='0.0.2',

    description='A simple tool to draw yout image to ascii code',

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
    install_requires=['pillow'],
    extras_require={
        'test': ['pytest', 'coverage']
    },
)
