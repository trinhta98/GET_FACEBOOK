#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests, re
from connection import config
token = config.token
payload = {'method':'get', 'access_token':token}

group_id = '368756226583661'

file = open('list_Email.txt', 'w', encoding='utf-8')
feeds = requests.get('https://graph.facebook.com/' + group_id + '/feed',params=payload).json()
while True:
    for feed in feeds['data']:
        try:
            feed_id = feed['id']
            comments = requests.get('https://graph.facebook.com/' + feed_id + '/comments',params=payload).json()
            try:
                for comment in comments['data']:
                    comment_msg = comment['message']
                    match = re.search(r"\w[\w._]+@\w+\.([A-Za-z]+\.)?[A-Za-z]{2,4}", comment_msg, re.I | re.U)
                    if match:  # nếu tồn tại chuỗi khớp
                        email = match.group()
                        print(email)
                        file.write(email + ', ')
            except KeyError:
                pass
        except KeyError:
            pass
    try:
        next_paging = feeds['paging']['next']
        feeds = requests.get(next_paging).json()
    except KeyError:
        file.close()
        exit(0)