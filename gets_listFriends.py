#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests,time
import facebook
import config
token = config.config_token
payload = {'method':'get','access_token':token}
graph = facebook.GraphAPI(token)
user_id = '100011762861034'
try:
    friends = graph.get_object(user_id + "/friends?limit=5000")
    friend_count = friends["summary"]['total_count']
    print("Tong cong co: " + str(friend_count) + " ban be:")
    i = 0
    for friend in friends['data']:
        i = i + 1
        print(str(i) + ". {0} có ID: {1}".format(friend['name'], friend['id']))
except:
    pass

# r_friend = testrequests.get("https://graph.facebook.com/" + user_id + "/friends?limit=5000", params=payload).json()
# print(r_friend)
# i = 0
# for friend in r_friend['data']:
#     i += 1
#     print(str(i) + ". {0} có ID: {1}".format(friend['name'], friend['id']))