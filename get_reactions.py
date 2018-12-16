# -*- coding: UTF-8 -*-
import requests, facebook
import config
token = config.config_token
payload = {'method':'get','access_token':token}
graph=facebook.GraphAPI(token)

user_id = '100004814822170'
id_post = '631950517207038'
reactions = requests.get('https://graph.facebook.com/'+id_post+'/reactions',params=payload).json()
print(reactions)
for reaction in reactions['data']:
    reaction_name = reaction['name']
    reaction_id = reaction['id']
    reaction_type = reaction['type']
    print(reaction_name + ' đã "' + reaction_type + '" bài viết')