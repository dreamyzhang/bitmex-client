# coding: utf-8

"""
    BitMEX API

    ## REST API for the BitMEX Trading Platform  [View Changelog](/app/apiChangelog)  ----  #### Getting Started   ##### Fetching Data  All REST endpoints are documented below. You can try out any query right from this interface.  Most table queries accept `count`, `start`, and `reverse` params. Set `reverse=true` to get rows newest-first.  Additional documentation regarding filters, timestamps, and authentication is available in [the main API documentation](https://www.bitmex.com/app/restAPI).  *All* table data is available via the [Websocket](/app/wsAPI). We highly recommend using the socket if you want to have the quickest possible data without being subject to ratelimits.  ##### Return Types  By default, all data is returned as JSON. Send `?_format=csv` to get CSV data or `?_format=xml` to get XML data.  ##### Trade Data Queries  *This is only a small subset of what is available, to get you started.*  Fill in the parameters and click the `Try it out!` button to try any of these queries.  * [Pricing Data](#!/Quote/Quote_get)  * [Trade Data](#!/Trade/Trade_get)  * [OrderBook Data](#!/OrderBook/OrderBook_getL2)  * [Settlement Data](#!/Settlement/Settlement_get)  * [Exchange Statistics](#!/Stats/Stats_history)  Every function of the BitMEX.com platform is exposed here and documented. Many more functions are available.  ##### Swagger Specification  [⇩ Swagger JSON](swagger.json)  ----  ## All API Endpoints  Click to expand a section. 

    OpenAPI spec version: 1.2.0
    Contact: support@bitmex.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class OrderBookL2(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'symbol': 'str',
        'id': 'float',
        'side': 'str',
        'size': 'float',
        'price': 'float'
    }

    attribute_map = {
        'symbol': 'symbol',
        'id': 'id',
        'side': 'side',
        'size': 'size',
        'price': 'price'
    }

    def __init__(self, symbol=None, id=None, side=None, size=None, price=None):
        """
        OrderBookL2 - a model defined in Swagger
        """

        self._symbol = None
        self._id = None
        self._side = None
        self._size = None
        self._price = None
        self.discriminator = None

        self.symbol = symbol
        self.id = id
        self.side = side
        if size is not None:
          self.size = size
        if price is not None:
          self.price = price

    @property
    def symbol(self):
        """
        Gets the symbol of this OrderBookL2.

        :return: The symbol of this OrderBookL2.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """
        Sets the symbol of this OrderBookL2.

        :param symbol: The symbol of this OrderBookL2.
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")

        self._symbol = symbol

    @property
    def id(self):
        """
        Gets the id of this OrderBookL2.

        :return: The id of this OrderBookL2.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OrderBookL2.

        :param id: The id of this OrderBookL2.
        :type: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def side(self):
        """
        Gets the side of this OrderBookL2.

        :return: The side of this OrderBookL2.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """
        Sets the side of this OrderBookL2.

        :param side: The side of this OrderBookL2.
        :type: str
        """
        if side is None:
            raise ValueError("Invalid value for `side`, must not be `None`")

        self._side = side

    @property
    def size(self):
        """
        Gets the size of this OrderBookL2.

        :return: The size of this OrderBookL2.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this OrderBookL2.

        :param size: The size of this OrderBookL2.
        :type: float
        """

        self._size = size

    @property
    def price(self):
        """
        Gets the price of this OrderBookL2.

        :return: The price of this OrderBookL2.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this OrderBookL2.

        :param price: The price of this OrderBookL2.
        :type: float
        """

        self._price = price

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
        if not isinstance(other, OrderBookL2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
