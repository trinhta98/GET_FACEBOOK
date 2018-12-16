# -*- coding: UTF-8 -*-
import requests
import config
token = config.config_token
payload = {'method':'get','access_token':token}

id_user = '100000038484180'
r_feed = requests.get('https://graph.facebook.com/' + id_user + '/feed?', params=payload).json()
r_name = requests.get("https://graph.facebook.com/" + id_user + "?fields=name", params=payload).json()
print("Tổng số bài share của {} trong năm 2018: ".format(r_name['name']))
count_share = 0
dict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
while True:
    for data in r_feed['data']:
        created_time = data['created_time'][:10]
        created_time = created_time[8:10] + '/' + created_time[5:7] + '/' + created_time[:4]
        month_created = int(created_time[3:5])
        year_created = int(created_time[6:10])
        if(year_created == 2018):
            try:
                story = data['story']
                if(story == 'Kim Thanh Võ Thị shared a post.'):
                    dict[month_created] += 1
                elif(story == 'Kim Thanh Võ Thị shared a video.'):
                    dict[month_created] += 1
            except KeyError:
                pass
        else:
            for i in range (1, 13):
                print(" - Tổng số bài share trong tháng {} là: {}".format(i, dict[i]) )
            exit(0)
    try:
        next_paging = r_feed['paging']['next']
        r_feed = requests.get(next_paging).json()
    except KeyError:
        break