from setuptools import setup, find_packages

PROJECT = 'cloudcli'
VERSION = '2016.4.1'

setup(name=PROJECT,
      version=VERSION,
      description='cloud command line tools',
      url='https://github.com/Hawkgirl/cloudcli/',
      author='Hawkgirl',
      install_requires=['cliff'],
      maintainer='Hawkgril',
      maintainer_email='hawkgirlgit@gmail.com',
      license='BSD',
      packages=find_packages(),
      include_package_data=True,

      entry_points={
        'console_scripts': [
            'cloudcli = cloudcli.main:main'
        ],
        'cloudcli.client': [
	    'instance-list = cloudcli.instance:ListInstance',
	    'instance-show = cloudcli.instance:ShowInstance',
	    'token-create = cloudcli.token:TokenCreate',
	    'zombie-list = cloudcli.zombie:ZombieList',
	    'zombie-stats = cloudcli.zombie:ZombieStats'
        ],
	},

      zip_safe=False,
      platforms=['Any'],
      )
