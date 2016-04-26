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
	    'instance-list = cloudcli.instance:InstanceList',
	    'instance-show = cloudcli.instance:InstanceShow',
	    'hypervisor-list = cloudcli.hypervisor:HypervisorList',
	    'hypervisor-show = cloudcli.hypervisor:HypervisorShow',
	    'volume-list = cloudcli.volumes:VolumeList',
	    'volume-show = cloudcli.volumes:VolumeShow',
	    'service-list = cloudcli.services:ServicesList',
	    'token-create = cloudcli.token:TokenCreate',
	    'zombie-list = cloudcli.zombie:ZombieList',
	    'zombie-stats = cloudcli.zombie:ZombieStats',
	    'sensu-services = cloudcli.services:ServicesSensu',
	    'sensu-instances = cloudcli.instance:InstancesSensu',
	    'sensu-hypervisor = cloudcli.hypervisor:HypervisorSensu',
	    'sensu-volumes = cloudcli.volumes:VolumeSensu',
	    'graphite-metrics = cloudcli.graphite:GraphiteMetrics'
        ],
	},

      zip_safe=False,
      platforms=['Any'],
      )
