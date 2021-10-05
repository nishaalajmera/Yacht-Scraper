from setuptools import setup
from setuptools import find_packages

setup(
    name = 'yacht_scraper',
    version = '0.0.2',
    description = 'Package that allows scraping of yacht data from boat24.com',
    url = 'https://github.com/nishaalajmera/Yacht_scraper.git',
    author = 'Nishaal Ajmera',
    licence = 'MIT',
    packages = find_packages(),
    install_requires = ['selenium','pandas','tqdm']
)