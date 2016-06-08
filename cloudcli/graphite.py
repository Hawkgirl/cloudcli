from cliff.lister import Lister
import datetime
import time

class GraphiteMetrics(Lister):
    """List cloud metrics in Graphite format"""

    @property
    def formatter_default(self):
        return 'value'

    def take_action(self, args):
	metrics = self.app.cloud_obj.resources.list_metrics()
        return (('', '', '' ), ((metric.name, metric.value, metric.timestamp) for metric in metrics))

class GraphiteInstanceMetrics(Lister):
    """List Instance usage metrics in Graphite format"""

    @property
    def formatter_default(self):
        return 'value'

    def take_action(self, args):
	instances = self.app.cloud_obj.compute.list_instances()
	lst = []
	end = datetime.datetime.now()
	start= end - datetime.timedelta(hours=6)

	for i in instances:
		tenant_name = 'NA'
		if i.tenant_name:
			tenant_name = i.tenant_name.replace('.', '_').replace('@', '_')
		name = 'openstack.tenant.'+i.tenant_id+'.'+str(tenant_name)+'.instance.'+i.id+'.'+str(i.name)+'.cpu'
		name = str(name)
		cpu_usage = i.cpu_usage(start_time = start, end_time = end, count=12)
		for u in cpu_usage:
			timestamp = datetime.datetime.strptime(u['end_time'], "%Y-%m-%dT%H:%M:%S")
			value = u['avg']
			delta = timestamp - datetime.datetime.utcfromtimestamp(0)
			t = (name,value,int(delta.total_seconds()))
			lst.append(t)
	return (('','',''), tuple(lst))
