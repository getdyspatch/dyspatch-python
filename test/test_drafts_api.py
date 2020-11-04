# coding: utf-8

"""
    Dyspatch API

    # Introduction  The Dyspatch API is based on the REST paradigm, and features resource based URLs with standard HTTP response codes to indicate errors. We use standard HTTP authentication and request verbs, and all responses are JSON formatted. See our [Implementation Guide](https://docs.dyspatch.io/development/implementing_dyspatch/) for more details on how to implement Dyspatch.  ## API Client Libraries Dyspatch provides API Clients for popular languages and web frameworks.  - [Java](https://github.com/getdyspatch/dyspatch-java) - [Javascript](https://github.com/getdyspatch/dyspatch-javascript) - [Python](https://github.com/getdyspatch/dyspatch-python) - [C#](https://github.com/getdyspatch/dyspatch-dotnet) - [Go](https://github.com/getdyspatch/dyspatch-golang) - [Ruby](https://github.com/getdyspatch/dyspatch-ruby)   # noqa: E501

    The version of the OpenAPI document: 2020.08
    Contact: support@dyspatch.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import dyspatch_client
from dyspatch_client.api.drafts_api import DraftsApi  # noqa: E501
from dyspatch_client.rest import ApiException


class TestDraftsApi(unittest.TestCase):
    """DraftsApi unit test stubs"""

    def setUp(self):
        self.api = dyspatch_client.api.drafts_api.DraftsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_localization(self):
        """Test case for delete_localization

        Remove a localization  # noqa: E501
        """
        pass

    def test_get_draft_by_id(self):
        """Test case for get_draft_by_id

        Get Draft by ID  # noqa: E501
        """
        pass

    def test_get_draft_localization_keys(self):
        """Test case for get_draft_localization_keys

        Get localization keys  # noqa: E501
        """
        pass

    def test_get_drafts(self):
        """Test case for get_drafts

        List Drafts  # noqa: E501
        """
        pass

    def test_get_localization_for_draft(self):
        """Test case for get_localization_for_draft

        Get localizations on a draft  # noqa: E501
        """
        pass

    def test_save_localization(self):
        """Test case for save_localization

        Create or update a localization  # noqa: E501
        """
        pass

    def test_set_translation(self):
        """Test case for set_translation

        Set translations for language  # noqa: E501
        """
        pass

    def test_submit_draft_for_approval(self):
        """Test case for submit_draft_for_approval

        Submit the draft for approval  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
