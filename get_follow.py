# -*- coding: UTF-8 -*-
import requests, json, facebook
import config
token = config.config_token
payload = {'method':'get','access_token':token}
graph=facebook.GraphAPI(token)

subcribers = requests.get('https://graph.facebook.com/me/subscribers?limit=5000',params=payload).json()

print(subcribers)
try:
    subcribers_count = subcribers['summary']['total_count']
    print('Tổng số người follow: {}'.format(subcribers_count))
    i = 0
    for subcriber in subcribers['data']:
        i += 1
        subcriber_name = subcriber['name']
        subcriber_id = subcriber['id']
        print(str(i) + '. ' + subcriber_name + 'có ID: {}'.format(subcriber_id))
except KeyError:
    pass


