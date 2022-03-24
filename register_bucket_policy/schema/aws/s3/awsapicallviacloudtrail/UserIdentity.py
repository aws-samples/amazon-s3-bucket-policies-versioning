# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.s3.awsapicallviacloudtrail.SessionContext import SessionContext  # noqa: F401,E501

class UserIdentity(object):


    _types = {
        'sessionContext': 'SessionContext',
        'accessKeyId': 'str',
        'accountId': 'str',
        'principalId': 'str',
        'type': 'str',
        'arn': 'str'
    }

    _attribute_map = {
        'sessionContext': 'sessionContext',
        'accessKeyId': 'accessKeyId',
        'accountId': 'accountId',
        'principalId': 'principalId',
        'type': 'type',
        'arn': 'arn'
    }

    def __init__(self, sessionContext=None, accessKeyId=None, accountId=None, principalId=None, type=None, arn=None):  # noqa: E501
        self._sessionContext = None
        self._accessKeyId = None
        self._accountId = None
        self._principalId = None
        self._type = None
        self._arn = None
        self.discriminator = None
        self.sessionContext = sessionContext
        self.accessKeyId = accessKeyId
        self.accountId = accountId
        self.principalId = principalId
        self.type = type
        self.arn = arn


    @property
    def sessionContext(self):

        return self._sessionContext

    @sessionContext.setter
    def sessionContext(self, sessionContext):


        self._sessionContext = sessionContext


    @property
    def accessKeyId(self):

        return self._accessKeyId

    @accessKeyId.setter
    def accessKeyId(self, accessKeyId):


        self._accessKeyId = accessKeyId


    @property
    def accountId(self):

        return self._accountId

    @accountId.setter
    def accountId(self, accountId):


        self._accountId = accountId


    @property
    def principalId(self):

        return self._principalId

    @principalId.setter
    def principalId(self, principalId):


        self._principalId = principalId


    @property
    def type(self):

        return self._type

    @type.setter
    def type(self, type):


        self._type = type


    @property
    def arn(self):

        return self._arn

    @arn.setter
    def arn(self, arn):


        self._arn = arn

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
        if issubclass(UserIdentity, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, UserIdentity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

