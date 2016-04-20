from cliff.lister import Lister

class GraphiteMetrics(Lister):
    """List cloud metrics in Graphite format"""


    def take_action(self, args):
	metrics = self.app.cloud_obj.resources.list_metrics()
        return (('Metric Name', 'Metric Value', 'Timestamp' ),
                ((metric.name, metric.value, metric.timestamp) for metric in metrics)
                )
