# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class RequestParameters(object):


    _types = {
        'bucketName': 'str',
        'legal_hold': 'str',
        'key': 'str',
        'retention': 'str'
    }

    _attribute_map = {
        'bucketName': 'bucketName',
        'legal_hold': 'legal-hold',
        'key': 'key',
        'retention': 'retention'
    }

    def __init__(self, bucketName=None, legal_hold=None, key=None, retention=None):  # noqa: E501
        self._bucketName = None
        self._legal_hold = None
        self._key = None
        self._retention = None
        self.discriminator = None
        self.bucketName = bucketName
        self.legal_hold = legal_hold
        self.key = key
        self.retention = retention


    @property
    def bucketName(self):

        return self._bucketName

    @bucketName.setter
    def bucketName(self, bucketName):


        self._bucketName = bucketName


    @property
    def legal_hold(self):

        return self._legal_hold

    @legal_hold.setter
    def legal_hold(self, legal_hold):


        self._legal_hold = legal_hold


    @property
    def key(self):

        return self._key

    @key.setter
    def key(self, key):


        self._key = key


    @property
    def retention(self):

        return self._retention

    @retention.setter
    def retention(self, retention):


        self._retention = retention

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
        if issubclass(RequestParameters, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, RequestParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

