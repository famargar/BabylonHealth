
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import babylonHealth

config = {
    'description': 'Babylon health ',
    'author': 'FabrizioMargaroli',
    'version': babylonHealth.__version__,
    'download_url': 'Where to download it.',
    'url': '',
    'author_email': '',
    'install_requires': ['bottle'],
    'packages': ['babylonHealth'],
    'scripts': [],
    'name': 'BabylonHealth',
    'long_description': open('README.md').read(),
    'package_data': {
        'babylonHealth': ['views/*.tpl'],
       },
        'include_package_data': True
}

setup(**config)