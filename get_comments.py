# -*- coding: UTF-8 -*-
import requests, json, facebook
import config
token = config.config_token
payload = {'method':'get','access_token':token}
graph=facebook.GraphAPI(token)
comments = requests.get("https://graph.facebook.com/634301103638646/comments", params=payload).json()
print(comments)
for comment in comments['data']:
    comment_name = comment['from']['name']
    comment_id = comment['from']['id']
    comment_message = comment['message']
    print(comment_name + ' đã comment với nội dung: ' + comment_message)
