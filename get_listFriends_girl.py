#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import config
token = config.config_token
payload = {'method':'get','access_token':token}
user_id = '100013748687797'

list = []
friends = requests.get("https://graph.facebook.com/"+ user_id + "/friends?limit=5000", params=payload).json()
for friend in friends['data']:
    friend_id = friend['id']
    gender = requests.get("https://graph.facebook.com/"+ friend_id + "?fields=gender", params=payload).json()
    try:
        if(gender['gender'] == 'female'):
            list.append(friend_id)
            print(friend['name'])
    except KeyError:
        pass
print(list)


