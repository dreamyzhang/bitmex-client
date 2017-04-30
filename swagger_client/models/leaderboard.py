# coding: utf-8

"""
    BitMEX API

    ## REST API for the BitMEX Trading Platform  [Changelog](/app/apiChangelog)  ----  #### Getting Started   ##### Fetching Data  All REST endpoints are documented below. You can try out any query right from this interface.  Most table queries accept `count`, `start`, and `reverse` params. Set `reverse=true` to get rows newest-first.  Additional documentation regarding filters, timestamps, and authentication is available in [the main API documentation](https://www.bitmex.com/app/restAPI).  *All* table data is available via the [Websocket](/app/wsAPI). We highly recommend using the socket if you want to have the quickest possible data without being subject to ratelimits.  ##### Return Types  By default, all data is returned as JSON. Send `?_format=csv` to get CSV data or `?_format=xml` to get XML data.  ##### Trade Data Queries  *This is only a small subset of what is available, to get you started.*  Fill in the parameters and click the `Try it out!` button to try any of these queries.  * [Pricing Data](#!/Quote/Quote_get)  * [Trade Data](#!/Trade/Trade_get)  * [OrderBook Data](#!/OrderBook/OrderBook_getL2)  * [Settlement Data](#!/Settlement/Settlement_get)  * [Exchange Statistics](#!/Stats/Stats_history)  Every function of the BitMEX.com platform is exposed here and documented. Many more functions are available.  ----  ## All API Endpoints  Click to expand a section. 

    OpenAPI spec version: 1.2.0
    Contact: support@bitmex.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Leaderboard(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, is_real_name=None, is_me=None, profit=None):
        """
        Leaderboard - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'is_real_name': 'bool',
            'is_me': 'bool',
            'profit': 'float'
        }

        self.attribute_map = {
            'name': 'name',
            'is_real_name': 'isRealName',
            'is_me': 'isMe',
            'profit': 'profit'
        }

        self._name = None
        self._is_real_name = None
        self._is_me = None
        self._profit = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if name is not None:
          self.name = name
        if is_real_name is not None:
          self.is_real_name = is_real_name
        if is_me is not None:
          self.is_me = is_me
        if profit is not None:
          self.profit = profit

    @property
    def name(self):
        """
        Gets the name of this Leaderboard.

        :return: The name of this Leaderboard.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Leaderboard.

        :param name: The name of this Leaderboard.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def is_real_name(self):
        """
        Gets the is_real_name of this Leaderboard.

        :return: The is_real_name of this Leaderboard.
        :rtype: bool
        """
        return self._is_real_name

    @is_real_name.setter
    def is_real_name(self, is_real_name):
        """
        Sets the is_real_name of this Leaderboard.

        :param is_real_name: The is_real_name of this Leaderboard.
        :type: bool
        """

        self._is_real_name = is_real_name

    @property
    def is_me(self):
        """
        Gets the is_me of this Leaderboard.

        :return: The is_me of this Leaderboard.
        :rtype: bool
        """
        return self._is_me

    @is_me.setter
    def is_me(self, is_me):
        """
        Sets the is_me of this Leaderboard.

        :param is_me: The is_me of this Leaderboard.
        :type: bool
        """

        self._is_me = is_me

    @property
    def profit(self):
        """
        Gets the profit of this Leaderboard.

        :return: The profit of this Leaderboard.
        :rtype: float
        """
        return self._profit

    @profit.setter
    def profit(self, profit):
        """
        Sets the profit of this Leaderboard.

        :param profit: The profit of this Leaderboard.
        :type: float
        """

        self._profit = profit

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Leaderboard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
