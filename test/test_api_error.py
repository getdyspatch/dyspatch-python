# coding: utf-8

"""
    Dyspatch API

    # Introduction  The Dyspatch API is based on the REST paradigm and features resource based URLs with standard HTTP response codes to indicate errors. We use standard HTTP authentication and request verbs and all responses are JSON formatted. See our [Implementation Guide](https://docs.dyspatch.io/development/implementing_dyspatch/) for more details on how to implement Dyspatch.  ## API Client Libraries  Dyspatch provides API Clients for the following languages and web frameworks:  - [Java](https://github.com/getdyspatch/dyspatch-java) - [Javascript](https://github.com/getdyspatch/dyspatch-javascript) - [Python](https://github.com/getdyspatch/dyspatch-python) - [C#](https://github.com/getdyspatch/dyspatch-dotnet) - [Go](https://github.com/getdyspatch/dyspatch-golang) - [Ruby](https://github.com/getdyspatch/dyspatch-ruby)   # noqa: E501

    OpenAPI spec version: 2019.10
    Contact: support@dyspatch.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import dyspatch_client
from dyspatch_client.models.api_error import APIError  # noqa: E501
from dyspatch_client.rest import ApiException


class TestAPIError(unittest.TestCase):
    """APIError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAPIError(self):
        """Test APIError"""
        # FIXME: construct object with mandatory attributes with example values
        # model = dyspatch_client.models.api_error.APIError()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
