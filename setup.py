from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in core_js/__init__.py
from core_js import __version__ as version

setup(
	name="core_js",
	version=version,
	description="Justsigns Customization",
	author="Justsigns",
	author_email="dev@justsigns.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
