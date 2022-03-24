# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.s3.awsapicallviacloudtrail.LegalHoldInfo import LegalHoldInfo  # noqa: F401,E501
from schema.aws.s3.awsapicallviacloudtrail.RetentionInfo import RetentionInfo  # noqa: F401,E501

class ObjectRetentionInfo(object):


    _types = {
        'legalHoldInfo': 'LegalHoldInfo',
        'retentionInfo': 'RetentionInfo'
    }

    _attribute_map = {
        'legalHoldInfo': 'legalHoldInfo',
        'retentionInfo': 'retentionInfo'
    }

    def __init__(self, legalHoldInfo=None, retentionInfo=None):  # noqa: E501
        self._legalHoldInfo = None
        self._retentionInfo = None
        self.discriminator = None
        self.legalHoldInfo = legalHoldInfo
        self.retentionInfo = retentionInfo


    @property
    def legalHoldInfo(self):

        return self._legalHoldInfo

    @legalHoldInfo.setter
    def legalHoldInfo(self, legalHoldInfo):


        self._legalHoldInfo = legalHoldInfo


    @property
    def retentionInfo(self):

        return self._retentionInfo

    @retentionInfo.setter
    def retentionInfo(self, retentionInfo):


        self._retentionInfo = retentionInfo

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
        if issubclass(ObjectRetentionInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ObjectRetentionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

