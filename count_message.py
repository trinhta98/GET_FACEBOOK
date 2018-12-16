#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import facebook
token = 'EAAAAAYsX7TsBAESPOk5LYouTRfoCBkgRWcCc74Ctzr0JIbvF8TvUG2R9DiUGKD8Q4AK49ZAEwYZBmtSbCYq3RgKtSACV6kQYqf4ZArDGpkKHZB1zgacg3Mhzgu7bTZA6uPtMe7GwRScgRk9UY661BaKzc3fazZCN4zOdJgpqZBVNafJYN27ZA9dQk5xxPrfqIG1RzFebuJvhhV9T6kWo8OL1'#config.config_token

graph = facebook.GraphAPI(token)
payload={'method':'get','access_token':token}
threads = requests.get('https://graph.facebook.com/me/threads?fields=from&limit=5000&access_token', params=payload).json()
print(threads)
dem = 0
for i in threads['data']:
    id_mess = i['id']
    messages = requests.get('https://graph.facebook.com/' +id_mess+ '?limit=5000&access_token', params=payload).json()
    message_count = messages['message_count']
    name = messages['participants']['data'][0]['name']
    id = messages['participants']['data'][0]['id']
    print(str(dem) + '. Facebook: {} có ID: {} và ID cuộc trò chuyện: {} có tổng số tin nhắn: {}'.format(name, id,id_mess, message_count))
    dem +=1