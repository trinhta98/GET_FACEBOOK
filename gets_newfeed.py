#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import facebook
import config
token = config.config_token
graph = facebook.GraphAPI(token)
payload={'method':'get','access_token':token}

r = requests.get('https://graph.facebook.com/me/home?access_token=token', params=payload).json()
print(r)