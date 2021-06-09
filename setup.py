  
import setuptools

with open('README.md', 'r') as file:
	long_description = file.read()


setuptools.setup(
	name = 'preprocess_dl',
	include_package_data=True,
	version = '0.1.3',
	author = 'Aswin Kumar',
	author_email = 'aswinkumar.ec18@bitsathy.ac.in',
	description = 'This is preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	
