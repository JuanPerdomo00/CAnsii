from setuptools import setup

setup(
    name='cansii',
    version='0.2',
    packages=['cansii'],
    description='A Python library for terminal text colorization using ANSI escape codes.',
    author='Jakepys Perdomo',
    author_email='perdomojuan187@gmail.com',
    url='https://github.com/JuanPerdomo00/CAnsii',
    long_description=open('./README.md').read(),
    long_description_content_type='text/markdown',
    license='GPL-3.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
    ],
)

