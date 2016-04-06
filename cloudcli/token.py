from cliff.show import ShowOne

class TokenCreate(ShowOne):
	"""Creates new token"""

	def take_action(self, args):
		token  = self.app.cloud_obj.identity.create_token()

		return (('Token', 'Auth-URL', 'Project-Name', 'Username'), (token.id, token.auth_url, token.tenant_name, token.username ))
