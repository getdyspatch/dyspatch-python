# coding: utf-8

from __future__ import absolute_import

import unittest
import os

import dyspatch_client

version = "application/vnd.dyspatch.2019.10+json"

class TestDraftRead(unittest.TestCase):
    """DraftRead unit test stubs"""

    def setUp(self):
        key = os.environ['DYSPATCH_API_KEY']
        configuration = dyspatch_client.Configuration()
        configuration.api_key['Authorization'] = f'Bearer {key}'
        client = dyspatch_client.ApiClient(configuration)
        self.api = dyspatch_client.api.templates_api.TemplatesApi(client)

    def test_list_templates(self):
        templates = self.api.get_templates(version)
        print(templates)

        template = self.api.get_template_by_id(
            templates.data[0].id,
            "",
            version,
        )
        print(template)


if __name__ == '__main__':
    unittest.main()
