import requests
import json
import shopify
import os
import binascii


params = {
    'shop':'corpdiskdev.myshopify.com',
    'code': code,
    'timestamp': '1636739624',
    'hmac': hmac
}

shopify.Session.setup(api_key=SHOPIFY_API_KEY, secret=SHOPIFY_SECRET)

shop_url = "corpdiskdev.myshopify.com"
api_version = "2021-07"
state = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
redirect_url = "http://myapp.com/auth/shopify/callback"
scopes = ['read_products', 'read_orders']

newSession = shopify.Session(shop_url, api_version)
auth_url = newSession.create_permission_url(scopes, redirect_url, state)

session = shopify.Session(shop_url, api_version)
access_token = session.request_token(params)