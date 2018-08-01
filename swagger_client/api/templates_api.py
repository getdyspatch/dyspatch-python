# coding: utf-8

"""
    Dyspatch API

    # Introduction  The Dyspatch API is based on the REST paradigm, and features resource based URLs with standard HTTP response codes to indicate errors. We use standard HTTP authentication and request verbs, and all responses are JSON formatted. See our [Implementation Guide](https://docs.dyspatch.io/development/implementing_dyspatch/) for more details on how to implement Dyspatch.   # noqa: E501

    OpenAPI spec version: 2018.02
    Contact: support@dyspatch.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TemplatesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def templates_get(self, **kwargs):  # noqa: E501
        """List Templates  # noqa: E501

        Gets a list of Template Metadata objects for all templates. Up to 25 results returned before results are paginated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.templates_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: A cursor value used to retrieve a specific page from a paginated result set.
        :return: TemplatesRead
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.templates_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.templates_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def templates_get_with_http_info(self, **kwargs):  # noqa: E501
        """List Templates  # noqa: E501

        Gets a list of Template Metadata objects for all templates. Up to 25 results returned before results are paginated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.templates_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cursor: A cursor value used to retrieve a specific page from a paginated result set.
        :return: TemplatesRead
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method templates_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.dyspatch.2018.02+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/templates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TemplatesRead',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def templates_template_id_drafts_get(self, template_id, **kwargs):  # noqa: E501
        """List Template Drafts  # noqa: E501

        Gets a list of Template Draft Metadata objects for the specified template. Up to 25 results returned before results are paginated.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.templates_template_id_drafts_get(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: A template ID (required)
        :param str cursor: A cursor value used to retrieve a specific page from a paginated result set.
        :return: TemplateDraftsRead
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.templates_template_id_drafts_get_with_http_info(template_id, **kwargs)  # noqa: E501
        else:
            (data) = self.templates_template_id_drafts_get_with_http_info(template_id, **kwargs)  # noqa: E501
            return data

    def templates_template_id_drafts_get_with_http_info(self, template_id, **kwargs):  # noqa: E501
        """List Template Drafts  # noqa: E501

        Gets a list of Template Draft Metadata objects for the specified template. Up to 25 results returned before results are paginated.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.templates_template_id_drafts_get_with_http_info(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: A template ID (required)
        :param str cursor: A cursor value used to retrieve a specific page from a paginated result set.
        :return: TemplateDraftsRead
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template_id', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method templates_template_id_drafts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params or
                params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling `templates_template_id_drafts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_id' in params:
            path_params['templateId'] = params['template_id']  # noqa: E501

        query_params = []
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.dyspatch.2018.02+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/templates/{templateId}/drafts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TemplateDraftsRead',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def templates_template_id_drafts_template_draft_id_get(self, template_draft_id, template_id, **kwargs):  # noqa: E501
        """Get a Draft  # noqa: E501

        Gets a Draft object of a Template. This endpoint provides access to unpublished Template drafts. Note that accessing invalid template drafts   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.templates_template_id_drafts_template_draft_id_get(template_draft_id, template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_draft_id: A draft ID (required)
        :param str template_id: A template ID (required)
        :return: TemplateDraftRead
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.templates_template_id_drafts_template_draft_id_get_with_http_info(template_draft_id, template_id, **kwargs)  # noqa: E501
        else:
            (data) = self.templates_template_id_drafts_template_draft_id_get_with_http_info(template_draft_id, template_id, **kwargs)  # noqa: E501
            return data

    def templates_template_id_drafts_template_draft_id_get_with_http_info(self, template_draft_id, template_id, **kwargs):  # noqa: E501
        """Get a Draft  # noqa: E501

        Gets a Draft object of a Template. This endpoint provides access to unpublished Template drafts. Note that accessing invalid template drafts   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.templates_template_id_drafts_template_draft_id_get_with_http_info(template_draft_id, template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_draft_id: A draft ID (required)
        :param str template_id: A template ID (required)
        :return: TemplateDraftRead
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template_draft_id', 'template_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method templates_template_id_drafts_template_draft_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_draft_id' is set
        if ('template_draft_id' not in params or
                params['template_draft_id'] is None):
            raise ValueError("Missing the required parameter `template_draft_id` when calling `templates_template_id_drafts_template_draft_id_get`")  # noqa: E501
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params or
                params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling `templates_template_id_drafts_template_draft_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_draft_id' in params:
            path_params['templateDraftId'] = params['template_draft_id']  # noqa: E501
        if 'template_id' in params:
            path_params['templateId'] = params['template_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.dyspatch.2018.02+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/templates/{templateId}/drafts/{templateDraftId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TemplateDraftRead',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def templates_template_id_get(self, template_id, **kwargs):  # noqa: E501
        """Get Template by ID  # noqa: E501

        Gets a template object with the matching ID. If the template has published content the \"compiled\" field will contain the template .  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.templates_template_id_get(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: A template ID (required)
        :return: TemplateRead
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.templates_template_id_get_with_http_info(template_id, **kwargs)  # noqa: E501
        else:
            (data) = self.templates_template_id_get_with_http_info(template_id, **kwargs)  # noqa: E501
            return data

    def templates_template_id_get_with_http_info(self, template_id, **kwargs):  # noqa: E501
        """Get Template by ID  # noqa: E501

        Gets a template object with the matching ID. If the template has published content the \"compiled\" field will contain the template .  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.templates_template_id_get_with_http_info(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: A template ID (required)
        :return: TemplateRead
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method templates_template_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_id' is set
        if ('template_id' not in params or
                params['template_id'] is None):
            raise ValueError("Missing the required parameter `template_id` when calling `templates_template_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_id' in params:
            path_params['templateId'] = params['template_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.dyspatch.2018.02+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/templates/{templateId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TemplateRead',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
