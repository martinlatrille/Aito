from distutils.core import setup

setup(
  name = 'Aito',
  packages = ['libaito', 'libaito.test_sets'],
  scripts = ['bin/aito'],
  version = '0.5.6',
  description = 'Ultra-lightweight test suite focused on REST API end-to-end tests.',
  author = 'Martin Latrille',
  author_email = 'martinlatrille@live.fr',
  url = 'https://github.com/martinlatrille/Aito', # use the URL to the github repo
  download_url = 'https://github.com/martinlatrille/Aito/tarball/0.5', # I'll explain this in a second
  keywords = ['testing', 'REST', 'api', 'end-to-end'], # arbitrary keywords
  classifiers = [],
  install_requires = [
    "requests >= 2.6.0",
  ],
)
