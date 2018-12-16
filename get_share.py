# -*- coding: UTF-8 -*-
import requests, facebook
import config
token = config.config_token
graph = facebook.GraphAPI(token)
payload = {'method':'get','access_token':token}

id_user = '100002781549119'
feeds = requests.get('https://graph.facebook.com/' + id_user + '/feed?', params=payload).json()
print(feeds)
name = requests.get("https://graph.facebook.com/" + id_user + "?fields=name", params=payload).json()
print("Tổng số lượt được share trên trang cá nhân {} trong năm 2018 là: ".format(name['name']))
share = 0
dict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
while True:
    for feed in feeds['data']:
        created_time = feed['created_time'][:10]
        created_time = created_time[8:10] + '/' + created_time[5:7] + '/' + created_time[:4]
        month_created = int(created_time[3:5])
        year_created = int(created_time[6:10])
        if (year_created == 2018):
            try:
                share = feed['shares']['count']
                dict[month_created] += share
            except KeyError:
                pass
        else:
            for i in range (1, 13):
                print(" - Tổng số bài share trong tháng {} là: {}".format(i, dict[i]) )
            exit(0)
    try:
        next_paging = feeds['paging']['next']
        feeds = requests.get(next_paging).json()
    except KeyError:
        break