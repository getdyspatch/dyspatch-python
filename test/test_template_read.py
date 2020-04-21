# coding: utf-8

"""
    Dyspatch API

    # Introduction The Dyspatch API is based on the REST paradigm, and features resource based URLs with standard HTTP response codes to indicate errors. We use standard HTTP authentication and request verbs, and all responses are JSON formatted. See our [Implementation Guide](https://docs.dyspatch.io/development/implementing_dyspatch/) for more details on how to implement Dyspatch. ## API Client Libraries Dyspatch provides API Clients for popular languages and web frameworks. - [Java](https://github.com/getdyspatch/dyspatch-java) - [Javascript](https://github.com/getdyspatch/dyspatch-javascript) - [Python](https://github.com/getdyspatch/dyspatch-python) - [C#](https://github.com/getdyspatch/dyspatch-dotnet) - [Go](https://github.com/getdyspatch/dyspatch-golang) - [Ruby](https://github.com/getdyspatch/dyspatch-ruby)   # noqa: E501

    The version of the OpenAPI document: 2020.04
    Contact: support@dyspatch.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import dyspatch_client
from dyspatch_client.models.template_read import TemplateRead  # noqa: E501
from dyspatch_client.rest import ApiException


class TestTemplateRead(unittest.TestCase):
    """TemplateRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTemplateRead(self):
        """Test TemplateRead"""
        # FIXME: construct object with mandatory attributes with example values
        # model = dyspatch_client.models.template_read.TemplateRead()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
