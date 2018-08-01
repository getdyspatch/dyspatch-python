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

from swagger_client.models.language_id import LanguageId  # noqa: F401,E501
from swagger_client.models.localization_id import LocalizationId  # noqa: F401,E501
from swagger_client.models.localization_name import LocalizationName  # noqa: F401,E501
from swagger_client.models.localization_url import LocalizationUrl  # noqa: F401,E501


class LocalizationMetaRead(object):
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
        'id': 'LocalizationId',
        'language': 'LanguageId',
        'name': 'LocalizationName',
        'url': 'LocalizationUrl'
    }

    attribute_map = {
        'id': 'id',
        'language': 'language',
        'name': 'name',
        'url': 'url'
    }

    def __init__(self, id=None, language=None, name=None, url=None):  # noqa: E501
        """LocalizationMetaRead - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._language = None
        self._name = None
        self._url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if language is not None:
            self.language = language
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this LocalizationMetaRead.  # noqa: E501


        :return: The id of this LocalizationMetaRead.  # noqa: E501
        :rtype: LocalizationId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LocalizationMetaRead.


        :param id: The id of this LocalizationMetaRead.  # noqa: E501
        :type: LocalizationId
        """

        self._id = id

    @property
    def language(self):
        """Gets the language of this LocalizationMetaRead.  # noqa: E501


        :return: The language of this LocalizationMetaRead.  # noqa: E501
        :rtype: LanguageId
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this LocalizationMetaRead.


        :param language: The language of this LocalizationMetaRead.  # noqa: E501
        :type: LanguageId
        """

        self._language = language

    @property
    def name(self):
        """Gets the name of this LocalizationMetaRead.  # noqa: E501


        :return: The name of this LocalizationMetaRead.  # noqa: E501
        :rtype: LocalizationName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LocalizationMetaRead.


        :param name: The name of this LocalizationMetaRead.  # noqa: E501
        :type: LocalizationName
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this LocalizationMetaRead.  # noqa: E501


        :return: The url of this LocalizationMetaRead.  # noqa: E501
        :rtype: LocalizationUrl
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this LocalizationMetaRead.


        :param url: The url of this LocalizationMetaRead.  # noqa: E501
        :type: LocalizationUrl
        """

        self._url = url

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
        if not isinstance(other, LocalizationMetaRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
