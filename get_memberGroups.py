#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests, time
token = 'EAAAAAYsX7TsBABg1uaJ1cP03y3uPtB9hsRaJ89K26edSb7ye61ZCxTqCTYQ1wPdmVO2LnNsj9UYC2a7JX0AJZAMydZBIFHmoS1Pg317i42qWYXDigcMnHjUnZAcZC4kzboZCsjYHzcNiSc7N0rMHXzeZBjxh9rz5CUmTHw2Wz2Fxt11X3M376nikQfqe1PxvMbEBDc5Kr9AQbXZAlXv9MLj1'
payload = {'method':'get','access_token':token}

members = requests.get("https://graph.facebook.com/229059537247539/members?limit=100",params=payload).json()
print(members)
cmt_id = '2184795401795601'
mem_id ='100017455715081'
cmt = ' @['+mem_id+':0]'
payload2 = {'method': 'post', 'access_token': token, 'message': cmt}
r2 = requests.get("https://graph.facebook.com/" + cmt_id + "/comments", params=payload2).json()
print(r2)
# for member in members['data']:
#     mem_id = member['id']
#
#     payload2 = {'method': 'post', 'access_token': token, 'message': cmt}
#     r2 = testrequests.get("https://graph.facebook.com/" + cmt_id + "/comments", params=payload2).json()
#     print(cmt)
#     time.sleep(1)
