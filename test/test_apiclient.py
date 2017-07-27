# coding: utf-8

"""
    BitMEX API

    ## REST API for the BitMEX Trading Platform  [Changelog](/app/apiChangelog)  ----  #### Getting Started   ##### Fetching Data  All REST endpoints are documented below. You can try out any query right from this interface.  Most table queries accept `count`, `start`, and `reverse` params. Set `reverse=true` to get rows newest-first.  Additional documentation regarding filters, timestamps, and authentication is available in [the main API documentation](https://www.bitmex.com/app/restAPI).  *All* table data is available via the [Websocket](/app/wsAPI). We highly recommend using the socket if you want to have the quickest possible data without being subject to ratelimits.  ##### Return Types  By default, all data is returned as JSON. Send `?_format=csv` to get CSV data or `?_format=xml` to get XML data.  ##### Trade Data Queries  *This is only a small subset of what is available, to get you started.*  Fill in the parameters and click the `Try it out!` button to try any of these queries.  * [Pricing Data](#!/Quote/Quote_get)  * [Trade Data](#!/Trade/Trade_get)  * [OrderBook Data](#!/OrderBook/OrderBook_getL2)  * [Settlement Data](#!/Settlement/Settlement_get)  * [Exchange Statistics](#!/Stats/Stats_history)  Every function of the BitMEX.com platform is exposed here and documented. Many more functions are available.  ----  ## All API Endpoints  Click to expand a section.

    OpenAPI spec version: 1.2.0
    Contact: jose.oliveros.1983@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import bitmex_client
from bitmex_client.rest import ApiException
from bitmex_client import ApiClient, Configuration


class TestApiClient(unittest.TestCase):
    """ ApiClient unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApiClient_update_params_for_auth(self):
        apiKey = 'LAqUlngMIQkIUjXMUreyu3qn'
        apiSecret = 'chNOOS4KvNXR_Xq4k4c9qsfoKWvnDecLATCRlcBwyKDYnWgO'
        apiSignature = '65f9cfd2b86ed975f59331b26a79b84cab404fa603d09232604fce6275cbb98c'
        auth_settings = ['apiKey', 'apiNonce', 'apiSignature']
        method = 'POST'
        path = '/api/v1/order'
        nonce = 1429631577995
        post_params = [('symbol', 'XBTM15'),
                       ('price', 219.0),
                       ('clOrdID', 'mm_bitmex_1a/oemUeQ4CAJZgP3fjHsA'),
                       ('orderQty', 98)]

        headers = dict()
        config = Configuration()
        config.api_key['api-key'] = apiKey
        config.api_key['api-secret'] = apiSecret
        config.api_key['nonce'] = str(nonce)
        api = ApiClient(config)

        api.update_params_for_auth(method,
                                   path,
                                   headers,
                                   post_params,
                                   auth_settings)

        assert apiSignature == headers['api-signature']


if __name__ == '__main__':
    unittest.main()
