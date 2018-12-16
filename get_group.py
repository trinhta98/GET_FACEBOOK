# -*- coding: UTF-8 -*-
import requests, json, facebook
import config

token = config.config_token
payload = {'method':'get','access_token':token}
graph=facebook.GraphAPI(token)

user_id = '100004906542709'
user_id = '100005863156117'
user_id = '100005383896449'
r_groups = requests.get('https://graph.facebook.com/' + user_id + '/groups', params=payload).json()
print(r_groups)
r_name = requests.get("https://graph.facebook.com/" + user_id + "?fields=name", params=payload).json()
print('Các groups mà {} đã tham gia là: '.format(r_name['name']))
i = 0
for group in r_groups['data']:
    i += 1
    group_name = group['name']
    group_id = group['id']
    group_privacy = group['privacy']
    print(str(i) + '. Group ' + group_privacy + ' : ' + group_name + ' có ID: ' + group_id)