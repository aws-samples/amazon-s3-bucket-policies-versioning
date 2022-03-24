# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class RetentionInfo(object):


    _types = {
        'lastModifiedTime': 'int',
        'retainUntilTime': 'int',
        'retainUntilMode': 'str'
    }

    _attribute_map = {
        'lastModifiedTime': 'lastModifiedTime',
        'retainUntilTime': 'retainUntilTime',
        'retainUntilMode': 'retainUntilMode'
    }

    def __init__(self, lastModifiedTime=None, retainUntilTime=None, retainUntilMode=None):  # noqa: E501
        self._lastModifiedTime = None
        self._retainUntilTime = None
        self._retainUntilMode = None
        self.discriminator = None
        self.lastModifiedTime = lastModifiedTime
        self.retainUntilTime = retainUntilTime
        self.retainUntilMode = retainUntilMode


    @property
    def lastModifiedTime(self):

        return self._lastModifiedTime

    @lastModifiedTime.setter
    def lastModifiedTime(self, lastModifiedTime):


        self._lastModifiedTime = lastModifiedTime


    @property
    def retainUntilTime(self):

        return self._retainUntilTime

    @retainUntilTime.setter
    def retainUntilTime(self, retainUntilTime):


        self._retainUntilTime = retainUntilTime


    @property
    def retainUntilMode(self):

        return self._retainUntilMode

    @retainUntilMode.setter
    def retainUntilMode(self, retainUntilMode):


        self._retainUntilMode = retainUntilMode

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
        if issubclass(RetentionInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, RetentionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

