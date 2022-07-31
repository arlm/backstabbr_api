from setuptools import setup, find_packages

with open('requirements.txt') as fh:
    requires = fh.read().splitlines()

setup(name='backstabbr_api',
		version='1.0.3',
		description='Web-scraper API and Discord Bot for the online diplomacy program Backstabbr',
		url='https://github.com/arlm/backstabbr_api',
		author='Arjun Khurana',
		author_email='afkhurana@gmail.com',
		license='MIT',
		packages=['backstabbr_api', 'backstabbr_bot'],
		install_requires=requires)
