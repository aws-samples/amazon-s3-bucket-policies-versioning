# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class Attributes(object):


    _types = {
        'mfaAuthenticated': 'str',
        'creationDate': 'datetime'
    }

    _attribute_map = {
        'mfaAuthenticated': 'mfaAuthenticated',
        'creationDate': 'creationDate'
    }

    def __init__(self, mfaAuthenticated=None, creationDate=None):  # noqa: E501
        self._mfaAuthenticated = None
        self._creationDate = None
        self.discriminator = None
        self.mfaAuthenticated = mfaAuthenticated
        self.creationDate = creationDate


    @property
    def mfaAuthenticated(self):

        return self._mfaAuthenticated

    @mfaAuthenticated.setter
    def mfaAuthenticated(self, mfaAuthenticated):


        self._mfaAuthenticated = mfaAuthenticated


    @property
    def creationDate(self):

        return self._creationDate

    @creationDate.setter
    def creationDate(self, creationDate):


        self._creationDate = creationDate

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self._types):
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
        if issubclass(Attributes, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Attributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

