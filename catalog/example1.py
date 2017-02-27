"""Example 1."""


# Code:
self.expires, self.signature = self._get_params()
query_params = (('AWSAccessKeyId', self.access_key),
                ('Expires', self.expires),
                ('Signature', self.signature))

for (key, value) in query_params:
    curl_request += ' --data {0}={1}'.format(key, value)
