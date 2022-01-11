from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.4.2.0'
DESCRIPTION = 'Simple random puns picker'
with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as fh:
    LONG_DESCRIPTION = '\n' + fh.read()


# Setting up
setup(
    name='pypuns',
    version=VERSION,
    url='https://github.com/PyPuns/PyPuns',
    author='Bunz',
    author_email='66bunz@gmail.com',
    
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=LONG_DESCRIPTION,

    packages=['pypuns', 'pypuns.puns'],
    include_package_data=True,
    
    install_requires=[],

    keywords=['python', 'puns', 'pypuns', 'chatbots', 'chat', 'jokes', 'random jokes', 'random joke', 'joke', 'pun', 'random pun', 'random puns'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Natural Language :: English',
        'Natural Language :: Italian',
        'Topic :: Software Development :: Build Tools',
        'Operating System :: OS Independent',
    ],

    project_urls={
        'Bug Reports': 'https://github.com/PyPuns/PyPuns/issues',
        'Funding': 'https://www.buymeacoffee.com/66bunz',
        'Say Thanks!': 'https://saythanks.io/to/66Bunz',
        'Source': 'https://github.com/PyPuns/PyPuns',
    },
)
