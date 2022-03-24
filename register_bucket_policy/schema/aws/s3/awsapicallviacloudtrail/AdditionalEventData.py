# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.s3.awsapicallviacloudtrail.ObjectRetentionInfo import ObjectRetentionInfo  # noqa: F401,E501

class AdditionalEventData(object):


    _types = {
        'objectRetentionInfo': 'ObjectRetentionInfo',
        'x_amz_id_2': 'str'
    }

    _attribute_map = {
        'objectRetentionInfo': 'objectRetentionInfo',
        'x_amz_id_2': 'x-amz-id-2'
    }

    def __init__(self, objectRetentionInfo=None, x_amz_id_2=None):  # noqa: E501
        self._objectRetentionInfo = None
        self._x_amz_id_2 = None
        self.discriminator = None
        self.objectRetentionInfo = objectRetentionInfo
        self.x_amz_id_2 = x_amz_id_2


    @property
    def objectRetentionInfo(self):

        return self._objectRetentionInfo

    @objectRetentionInfo.setter
    def objectRetentionInfo(self, objectRetentionInfo):


        self._objectRetentionInfo = objectRetentionInfo


    @property
    def x_amz_id_2(self):

        return self._x_amz_id_2

    @x_amz_id_2.setter
    def x_amz_id_2(self, x_amz_id_2):


        self._x_amz_id_2 = x_amz_id_2

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
        if issubclass(AdditionalEventData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AdditionalEventData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

