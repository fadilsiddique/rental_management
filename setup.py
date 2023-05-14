from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rental_management/__init__.py
from rental_management import __version__ as version

setup(
	name="rental_management",
	version=version,
	description="Manages rental of a business",
	author="Fadil",
	author_email="fadilsiddique@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
