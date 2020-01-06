# coding: utf-8

"""
    Dyspatch API

    # Introduction  The Dyspatch API is based on the REST paradigm, and features resource based URLs with standard HTTP response codes to indicate errors. We use standard HTTP authentication and request verbs, and all responses are JSON formatted. See our [Implementation Guide](https://docs.dyspatch.io/development/implementing_dyspatch/) for more details on how to implement Dyspatch.  ## API Client Libraries Dyspatch provides API Clients for popular languages and web frameworks.  - [Java](https://github.com/getdyspatch/dyspatch-java) - [Javascript](https://github.com/getdyspatch/dyspatch-javascript) - [Python](https://github.com/getdyspatch/dyspatch-python) - [C#](https://github.com/getdyspatch/dyspatch-dotnet) - [Go](https://github.com/getdyspatch/dyspatch-golang) - [Ruby](https://github.com/getdyspatch/dyspatch-ruby)    # noqa: E501

    The version of the OpenAPI document: 2019.10
    Contact: support@dyspatch.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from dyspatch_client.configuration import Configuration


class DraftRead(object):
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
        'id': 'str',
        'template': 'str',
        'name': 'str',
        'url': 'str',
        'compiled': 'CompiledRead',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'localizations': 'list[LocalizationMetaRead]'
    }

    attribute_map = {
        'id': 'id',
        'template': 'template',
        'name': 'name',
        'url': 'url',
        'compiled': 'compiled',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'localizations': 'localizations'
    }

    def __init__(self, id=None, template=None, name=None, url=None, compiled=None, created_at=None, updated_at=None, localizations=None, local_vars_configuration=None):  # noqa: E501
        """DraftRead - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._template = None
        self._name = None
        self._url = None
        self._compiled = None
        self._created_at = None
        self._updated_at = None
        self._localizations = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if template is not None:
            self.template = template
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if compiled is not None:
            self.compiled = compiled
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if localizations is not None:
            self.localizations = localizations

    @property
    def id(self):
        """Gets the id of this DraftRead.  # noqa: E501

        An opaque, unique identifier for a draft  # noqa: E501

        :return: The id of this DraftRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DraftRead.

        An opaque, unique identifier for a draft  # noqa: E501

        :param id: The id of this DraftRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def template(self):
        """Gets the template of this DraftRead.  # noqa: E501

        An opaque, unique identifier for a template  # noqa: E501

        :return: The template of this DraftRead.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this DraftRead.

        An opaque, unique identifier for a template  # noqa: E501

        :param template: The template of this DraftRead.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def name(self):
        """Gets the name of this DraftRead.  # noqa: E501

        The name of a draft  # noqa: E501

        :return: The name of this DraftRead.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DraftRead.

        The name of a draft  # noqa: E501

        :param name: The name of this DraftRead.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this DraftRead.  # noqa: E501

        The API url for a specific draft  # noqa: E501

        :return: The url of this DraftRead.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DraftRead.

        The API url for a specific draft  # noqa: E501

        :param url: The url of this DraftRead.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def compiled(self):
        """Gets the compiled of this DraftRead.  # noqa: E501


        :return: The compiled of this DraftRead.  # noqa: E501
        :rtype: CompiledRead
        """
        return self._compiled

    @compiled.setter
    def compiled(self, compiled):
        """Sets the compiled of this DraftRead.


        :param compiled: The compiled of this DraftRead.  # noqa: E501
        :type: CompiledRead
        """

        self._compiled = compiled

    @property
    def created_at(self):
        """Gets the created_at of this DraftRead.  # noqa: E501

        The time of initial creation  # noqa: E501

        :return: The created_at of this DraftRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DraftRead.

        The time of initial creation  # noqa: E501

        :param created_at: The created_at of this DraftRead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this DraftRead.  # noqa: E501

        The time of last update  # noqa: E501

        :return: The updated_at of this DraftRead.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DraftRead.

        The time of last update  # noqa: E501

        :param updated_at: The updated_at of this DraftRead.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def localizations(self):
        """Gets the localizations of this DraftRead.  # noqa: E501

        A list of the Template's available localizations  # noqa: E501

        :return: The localizations of this DraftRead.  # noqa: E501
        :rtype: list[LocalizationMetaRead]
        """
        return self._localizations

    @localizations.setter
    def localizations(self, localizations):
        """Sets the localizations of this DraftRead.

        A list of the Template's available localizations  # noqa: E501

        :param localizations: The localizations of this DraftRead.  # noqa: E501
        :type: list[LocalizationMetaRead]
        """

        self._localizations = localizations

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
        if not isinstance(other, DraftRead):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DraftRead):
            return True

        return self.to_dict() != other.to_dict()
