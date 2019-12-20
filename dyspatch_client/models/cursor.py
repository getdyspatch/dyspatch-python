# coding: utf-8

"""
    Dyspatch API

    # Introduction The Dyspatch API is based on the REST paradigm, and features resource based URLs with standard HTTP response codes to indicate errors. We use standard HTTP authentication and request verbs, and all responses are JSON formatted. See our [Implementation Guide](https://docs.dyspatch.io/development/implementing_dyspatch/) for more details on how to implement Dyspatch. ## API Client Libraries Dyspatch provides API Clients for popular languages and web frameworks. - [Java](https://github.com/getdyspatch/dyspatch-java) - [Javascript](https://github.com/getdyspatch/dyspatch-javascript) - [Python](https://github.com/getdyspatch/dyspatch-python) - [C#](https://github.com/getdyspatch/dyspatch-dotnet) - [Go](https://github.com/getdyspatch/dyspatch-golang) - [Ruby](https://github.com/getdyspatch/dyspatch-ruby)   # noqa: E501

    The version of the OpenAPI document: 2019.10
    Contact: support@dyspatch.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dyspatch_client.configuration import Configuration


class Cursor(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'next': 'str',
        'has_more': 'bool'
    }

    attribute_map = {
        'next': 'next',
        'has_more': 'hasMore'
    }

    def __init__(self, next=None, has_more=None, local_vars_configuration=None):  # noqa: E501
        """Cursor - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._next = None
        self._has_more = None
        self.discriminator = None

        if next is not None:
            self.next = next
        if has_more is not None:
            self.has_more = has_more

    @property
    def next(self):
        """Gets the next of this Cursor.  # noqa: E501

        A cursor to fetch the next page of results  # noqa: E501

        :return: The next of this Cursor.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this Cursor.

        A cursor to fetch the next page of results  # noqa: E501

        :param next: The next of this Cursor.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def has_more(self):
        """Gets the has_more of this Cursor.  # noqa: E501

        Whether there is a next page of results  # noqa: E501

        :return: The has_more of this Cursor.  # noqa: E501
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this Cursor.

        Whether there is a next page of results  # noqa: E501

        :param has_more: The has_more of this Cursor.  # noqa: E501
        :type: bool
        """

        self._has_more = has_more

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, Cursor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Cursor):
            return True

        return self.to_dict() != other.to_dict()
