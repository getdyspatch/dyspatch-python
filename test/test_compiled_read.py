# coding: utf-8

"""
    Dyspatch API

    # Introduction  The Dyspatch API is based on the REST paradigm, and features resource based URLs with standard HTTP response codes to indicate errors. We use standard HTTP authentication and request verbs, and all responses are JSON formatted. See our [Implementation Guide](https://docs.dyspatch.io/development/implementing_dyspatch/) for more details on how to implement Dyspatch.  ## API Client Libraries Dyspatch provides API Clients for popular languages and web frameworks.  - [Java](https://github.com/getdyspatch/dyspatch-java) - [Javascript](https://github.com/getdyspatch/dyspatch-javascript) - [Python](https://github.com/getdyspatch/dyspatch-python) - [C#](https://github.com/getdyspatch/dyspatch-dotnet) - [Go](https://github.com/getdyspatch/dyspatch-golang) - [Ruby](https://github.com/getdyspatch/dyspatch-ruby)   # noqa: E501

    The version of the OpenAPI document: 2020.04
    Contact: support@dyspatch.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import dyspatch_client
from dyspatch_client.models.compiled_read import CompiledRead  # noqa: E501
from dyspatch_client.rest import ApiException

class TestCompiledRead(unittest.TestCase):
    """CompiledRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CompiledRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dyspatch_client.models.compiled_read.CompiledRead()  # noqa: E501
        if include_optional :
            return CompiledRead(
                sender = 'Example', 
                reply_to = 'Example', 
                subject = 'YQ==', 
                html = 'YQ==', 
                text = 'YQ=='
            )
        else :
            return CompiledRead(
        )

    def testCompiledRead(self):
        """Test CompiledRead"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
