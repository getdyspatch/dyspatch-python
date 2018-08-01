# coding: utf-8

"""
    Dyspatch API

    # Introduction  The Dyspatch API is based on the REST paradigm, and features resource based URLs with standard HTTP response codes to indicate errors. We use standard HTTP authentication and request verbs, and all responses are JSON formatted. See our [Implementation Guide](https://docs.dyspatch.io/development/implementing_dyspatch/) for more details on how to implement Dyspatch.   # noqa: E501

    OpenAPI spec version: 2018.02
    Contact: support@dyspatch.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.cursor import Cursor  # noqa: F401,E501
from swagger_client.models.template_meta_read import TemplateMetaRead  # noqa: F401,E501


class TemplatesRead(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cursor': 'Cursor',
        'data': 'list[TemplateMetaRead]'
    }

    attribute_map = {
        'cursor': 'cursor',
        'data': 'data'
    }

    def __init__(self, cursor=None, data=None):  # noqa: E501
        """TemplatesRead - a model defined in Swagger"""  # noqa: E501

        self._cursor = None
        self._data = None
        self.discriminator = None

        if cursor is not None:
            self.cursor = cursor
        if data is not None:
            self.data = data

    @property
    def cursor(self):
        """Gets the cursor of this TemplatesRead.  # noqa: E501


        :return: The cursor of this TemplatesRead.  # noqa: E501
        :rtype: Cursor
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this TemplatesRead.


        :param cursor: The cursor of this TemplatesRead.  # noqa: E501
        :type: Cursor
        """

        self._cursor = cursor

    @property
    def data(self):
        """Gets the data of this TemplatesRead.  # noqa: E501

        A list of template metadata objects  # noqa: E501

        :return: The data of this TemplatesRead.  # noqa: E501
        :rtype: list[TemplateMetaRead]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TemplatesRead.

        A list of template metadata objects  # noqa: E501

        :param data: The data of this TemplatesRead.  # noqa: E501
        :type: list[TemplateMetaRead]
        """

        self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TemplatesRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
