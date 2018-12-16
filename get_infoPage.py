# -*- coding: UTF-8 -*-
import requests
import config
token = config.config_token
payload = {'method':'get','access_token':token}

page_id = '287751184688400'
infoPage = requests.get("https://graph.facebook.com/" + page_id,params=payload).json()
page_name = infoPage['name']
try:
    page_about = infoPage['about']
except KeyError:
    pass
try:
    page_products = infoPage['products']
except KeyError:
    pass
print("Pg: {} có ID: {} | {} | {}".format(page_name, page_id, page_about, page_products))

