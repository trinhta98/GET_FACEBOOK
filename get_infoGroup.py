# -*- coding: UTF-8 -*-
import requests
import config
token = config.config_token
payload = {'method':'get','access_token':token}

group_id = '591471944538665'
infoGroup = requests.get("https://graph.facebook.com/" + group_id,params=payload).json()
print(infoGroup)

