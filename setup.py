from setuptools import setup, find_packages

setup(
    name='chromalog',
    version='0.1.0',
    author='tutosrivegamer',
    author_email='msqlitesrmtrg@gmail.com',
    description='Un micromódulo para imprimir mensajes por consola con texto de color Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
