from cliff.lister import Lister

class ListInstance(Lister):
    """List orders."""

    def get_parser(self, prog_name):
        parser = super(ListInstance, self).get_parser(prog_name)
        parser.add_argument('--limit', '-l', default=10,
                            help='specify the limit to the number of items '
                                 'to list per page (default: %(default)s; '
                                 'maximum: 100)',
                            type=int)
        return parser

    def take_action(self, args):
	instances = self.app.cloud_obj.compute.list_instances()
        return (('ID', 'Name', 'Public IP', 'Size', 'State' ),
                ((instance.id, instance.name, instance.public_ip, instance.size, instance.state) for instance in instances)
                )
