#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import facebook
import config
token = config.config_token
graph = facebook.GraphAPI(token)
payload={'method':'get','access_token':token}
r=requests.get('https://graph.facebook.com/me/threads?fields=from&limit=5000&access_token', params=payload).json()
r2=requests.get('https://graph.facebook.com/'+'t_706568559541966'+'?limit=5000&access_token', params=payload).json()
messages = r2['messages']
data = messages['data']
list_img = []
for i in range (0, 25):
    try:
        data0 = data[i]
        attachments = data0['attachments']
        attachments_data = attachments['data']
        attachments_data0 = attachments_data[0]
        image_data = attachments_data0['image_data']
        url = image_data['url']
        list_img.append(url)
    except:
        pass

try:
    url_first = list_img[0]
    print('url facebook:  ' + url_first)
    url2 = ''
    while(url2 == ''):
        try:
            r3 = requests.post('https://0x2f0713.000webhostapp.com/php/anime-filter.php', data={'url': url_first}).json()
            messages = r3['messages']
            messages1 = messages[1]
            attachment = messages1['attachment']
            payload = attachment['payload']
            url2 = payload['url']
            print('url anime:  '+url2)
        except:
            pass
except:
    pass