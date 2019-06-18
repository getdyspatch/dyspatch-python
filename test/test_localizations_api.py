# coding: utf-8

"""
    Dyspatch API

    # Introduction  The Dyspatch API is based on the REST paradigm, and features resource based URLs with standard HTTP response codes to indicate errors. We use standard HTTP authentication and request verbs, and all responses are JSON formatted. See our [Implementation Guide](https://docs.dyspatch.io/development/implementing_dyspatch/) for more details on how to implement Dyspatch.  ## API Client Libraries  Dyspatch provides API Clients for popular languages and web frameworks.   - [Java](https://github.com/getdyspatch/dyspatch-java) - [Javascript](https://github.com/getdyspatch/dyspatch-javascript) - [Python](https://github.com/getdyspatch/dyspatch-python) - [C#](https://github.com/getdyspatch/dyspatch-dotnet) - [Go](https://github.com/getdyspatch/dyspatch-golang) - [Ruby](https://github.com/getdyspatch/dyspatch-ruby)   # noqa: E501

    OpenAPI spec version: 2019.03
    Contact: support@dyspatch.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import dyspatch_client
from api.localizations_api import LocalizationsApi  # noqa: E501
from dyspatch_client.rest import ApiException


class TestLocalizationsApi(unittest.TestCase):
    """LocalizationsApi unit test stubs"""

    def setUp(self):
        self.api = api.localizations_api.LocalizationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_localizations_localization_id_get(self):
        """Test case for localizations_localization_id_get

        Get Localization Object by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
