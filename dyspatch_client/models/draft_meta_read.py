# coding: utf-8

"""
    Dyspatch API

    # Introduction  The Dyspatch API is based on the REST paradigm and features resource based URLs with standard HTTP response codes to indicate errors. We use standard HTTP authentication and request verbs and all responses are JSON formatted. See our [Implementation Guide](https://docs.dyspatch.io/development/implementing_dyspatch/) for more details on how to implement Dyspatch.  ## API Client Libraries  Dyspatch provides API Clients for the following languages and web frameworks:  - [Java](https://github.com/getdyspatch/dyspatch-java) - [Javascript](https://github.com/getdyspatch/dyspatch-javascript) - [Python](https://github.com/getdyspatch/dyspatch-python) - [C#](https://github.com/getdyspatch/dyspatch-dotnet) - [Go](https://github.com/getdyspatch/dyspatch-golang) - [Ruby](https://github.com/getdyspatch/dyspatch-ruby)   # noqa: E501

    OpenAPI spec version: 2019.10
    Contact: support@dyspatch.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DraftMetaRead(object):
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
        'id': 'str',
        'template_id': 'str',
        'name': 'str',
        'description': 'str',
        'url': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'template_id': 'templateId',
        'name': 'name',
        'description': 'description',
        'url': 'url',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, id=None, template_id=None, name=None, description=None, url=None, created_at=None, updated_at=None):  # noqa: E501
        """DraftMetaRead - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._template_id = None
        self._name = None
        self._description = None
        self._url = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if template_id is not None:
            self.template_id = template_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if url is not None:
            self.url = url
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this DraftMetaRead.  # noqa: E501

        An opaque, unique identifier for a draft  # noqa: E501

        :return: The id of this DraftMetaRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DraftMetaRead.

        An opaque, unique identifier for a draft  # noqa: E501

        :param id: The id of this DraftMetaRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def template_id(self):
        """Gets the template_id of this DraftMetaRead.  # noqa: E501

        An opaque, unique identifier for a template  # noqa: E501

        :return: The template_id of this DraftMetaRead.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this DraftMetaRead.

        An opaque, unique identifier for a template  # noqa: E501

        :param template_id: The template_id of this DraftMetaRead.  # noqa: E501
        :type: str
        """

        self._template_id = template_id

    @property
    def name(self):
        """Gets the name of this DraftMetaRead.  # noqa: E501

        The name of a draft  # noqa: E501

        :return: The name of this DraftMetaRead.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DraftMetaRead.

        The name of a draft  # noqa: E501

        :param name: The name of this DraftMetaRead.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this DraftMetaRead.  # noqa: E501

        A description of the draft  # noqa: E501

        :return: The description of this DraftMetaRead.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DraftMetaRead.

        A description of the draft  # noqa: E501

        :param description: The description of this DraftMetaRead.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def url(self):
        """Gets the url of this DraftMetaRead.  # noqa: E501

        The API url for a specific draft  # noqa: E501

        :return: The url of this DraftMetaRead.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DraftMetaRead.

        The API url for a specific draft  # noqa: E501

        :param url: The url of this DraftMetaRead.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def created_at(self):
        """Gets the created_at of this DraftMetaRead.  # noqa: E501

        The time of initial creation  # noqa: E501

        :return: The created_at of this DraftMetaRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DraftMetaRead.

        The time of initial creation  # noqa: E501

        :param created_at: The created_at of this DraftMetaRead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this DraftMetaRead.  # noqa: E501

        The time of last update  # noqa: E501

        :return: The updated_at of this DraftMetaRead.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DraftMetaRead.

        The time of last update  # noqa: E501

        :param updated_at: The updated_at of this DraftMetaRead.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, DraftMetaRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other