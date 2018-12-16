# -*- coding: UTF-8 -*-
import requests, datetime, time
import config
token = config.config_token
payload = {'method':'get','access_token':token}

print("~~~~~~~~~~KIỂM TRA TƯƠNG TÁC~~~~~~~~~\n~~~~~~~~~~~~Cách tính điểm~~~~~~~~~~~\n-Reaction: 1đ\n-Comment:2đ\n-Rep-commment:1đ\n-Share: 3đ\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

user_id = '100002781549119'
user_id = input("Nhập User ID vào đây: ")
try:
    feeds = requests.get('https://graph.facebook.com/' +user_id + '/feed?', params=payload).json()
except:
    print("Mã truy cập hết hạn, liên hệ coder để lấy lại bản mới")
info = requests.get("https://graph.facebook.com/" + user_id + "?edges&access_token",params=payload).json()
name = info['name']
print("Facebook có ID {} : {}".format(user_id, name))
first_name = info['first_name']
dict_interactive = {}
dict_top_interactive = {}
dict_final = {}
key = 0
temp2 = 0
datetime_now = str(datetime.datetime.now().date())
while True:
    input_days = input("Nhập ngày bắt đầu cần kiểm tra tương tác (vd:20/10/2018): ")
    temp3 = 0
    if (len(input_days) != 10):
        print("Nhập không đúng mẫu!")
        temp3 = 1
    elif (int(input_days[6:10]) != 2018):
        print("Nhập ngày tháng năm của năm 2018")
        temp3 = 1
    elif(int(input_days[3:5]) > int(datetime_now[5:7])):
        print("Nhập ngày tháng nhỏ hơn tháng hiện tại")
        temp3 = 1
    elif (int(input_days[3:5]) == int(datetime_now[5:7])):
        if(int(input_days[:2]) > int(datetime_now[8:10])):
            print("Nhập ngày nhỏ hơn ngày hiện tại")
            temp3 = 1
    if(temp3 == 0):
        break
print("Bắt đầu kiểm tra tương tác...")
while True:
    for feed in feeds['data']:
        created_time = feed['created_time'][:10]
        created_time = created_time[8:10] + '/' + created_time[5:7] + '/' + created_time[:4]
        if (created_time != input_days):
            try:
                for comment in feed['comments']['data']:
                    cmt_id = comment['from']['id']
                    if (cmt_id != user_id):
                        if (key == 0):
                            key += 1
                            dict_interactive[key] = {}
                            dict_interactive[key]['id'] = cmt_id
                            dict_interactive[key]['count'] = 1
                        else:
                            temp = 0
                            for i in range(1, key + 1):
                                if (cmt_id == dict_interactive[i]['id']):
                                    dict_interactive[i]['count'] += 1
                                    temp = 1
                                    break
                            if (temp == 0):
                                key += 1
                                dict_interactive[key] = {}
                                dict_interactive[key]['id'] = cmt_id
                                dict_interactive[key]['count'] = 1
            except KeyError:
                pass


            feed_id = feed['id']
            comments = requests.get('https://graph.facebook.com/'+ feed_id +'/comments',params=payload).json()
            try:
                for comment in comments['data']:
                    cmt_id = comment['from']['id']
                    if (cmt_id != user_id):
                        if (key == 0):
                            key += 1
                            dict_interactive[key] = {}
                            dict_interactive[key]['id'] = cmt_id
                            dict_interactive[key]['count'] = 1
                        else:
                            temp = 0
                            for i in range(1, key + 1):
                                if (cmt_id == dict_interactive[i]['id']):
                                    dict_interactive[i]['count'] += 1
                                    temp = 1
                                    break
                            if (temp == 0):
                                key += 1
                                dict_interactive[key] = {}
                                dict_interactive[key]['id'] = cmt_id
                                dict_interactive[key]['count'] = 1
            except KeyError:
                pass

            reactions = requests.get('https://graph.facebook.com/' + feed_id + '/reactions', params=payload).json()
            try:
                for reaction in reactions['data']:
                    reaction_id = reaction['id']
                    if (reaction_id != user_id):
                        if (key == 0):
                            key += 1
                            dict_interactive[key] = {}
                            dict_interactive[key]['id'] = reaction_id
                            dict_interactive[key]['count'] = 1
                        else:
                            temp = 0
                            for i in range(1, key + 1):
                                if (reaction_id == dict_interactive[i]['id']):
                                    dict_interactive[i]['count'] += 1
                                    temp = 1
                                    break
                            if (temp == 0):
                                key += 1
                                dict_interactive[key] = {}
                                dict_interactive[key]['id'] = reaction_id
                                dict_interactive[key]['count'] = 1
            except KeyError:
                pass
        else:
            temp2 = 1
            break
    if(temp2 == 1):
        break
    else:
        try:
            next_paging = feeds['paging']['next']
            feeds = requests.get(next_paging).json()
        except KeyError:
            break

# print('1'+str(dict_interactive))
print("Đã kiểm tra xong.")
print("Bắt đầu tìm kiếm 10 người tương tác nhiều nhất...")

max = 1
for i in dict_interactive:
    if(i > max):
        max = i
max = int(max)
for j in range(1, 21):
    try:
        max_Count = dict_interactive[max]['count']
        max_Key = max
        max_ID = dict_interactive[max]['id']
        for i in dict_interactive:
            if (max_Count < dict_interactive[i]['count']):
                max_Count = dict_interactive[i]['count']
                max_ID = dict_interactive[i]['id']
                max_Key = i
        del dict_interactive[max_Key]
        dict_top_interactive[j] = {}
        dict_top_interactive[j]['id'] = max_ID
        dict_top_interactive[j]['count'] = max_Count
    except KeyError:
        pass

# print('2'+str(dict_top_interactive))
for i in dict_top_interactive:
    try:
        feeds = requests.get('https://graph.facebook.com/' + dict_top_interactive[i]['id'] + '/feed?',
                             params=payload).json()
        for feed in feeds['data']:
            created_time = feed['created_time'][:10]
            created_time = created_time[8:10] + '/' + created_time[5:7] + '/' + created_time[:4]
            if(int(created_time[3:5]) < int(input_days[3:5])):
                break
            else:
                if (int(created_time[:2]) < int(input_days[:2])):
                    break
                else:
                    if (created_time == input_days):
                        break
                    try:
                        share_by_name = feed['name']
                        if (share_by_name == first_name):
                            dict_top_interactive[i]['count'] += 3
                    except KeyError:
                        pass
    except KeyError:
        pass
# print('3'+str(dict_top_interactive))

max_CountB = dict_top_interactive[1]['count']
max_KeyB = 1
max_IDB = dict_top_interactive[1]['id']
for i in dict_top_interactive:
    if(dict_top_interactive[i]['count'] < max_CountB):
        max_CountB = dict_top_interactive[i]['count']
        max_KeyB = i
        max_IDB = dict_top_interactive[i]['id']
for j in range(1,21):
    try:
        max_Count = max_CountB
        max_Key = max_KeyB
        max_ID = max_IDB
        for i in dict_top_interactive:
            if (max_Count < dict_top_interactive[i]['count']):
                max_Count = dict_top_interactive[i]['count']
                max_ID = dict_top_interactive[i]['id']
                max_Key = i
        del dict_top_interactive[max_Key]
        dict_final[j] = {}
        dict_final[j]['id'] = max_ID
        dict_final[j]['count'] = max_Count
    except KeyError:
        pass
# print('4'+str(dict_final))
datetime_now = str(datetime.datetime.now().date())
datetime_now = datetime_now[8:10] + datetime_now[4:8] + datetime_now[:4]
datetime_now = datetime_now.split("-")
datetime_now = '/'.join(datetime_now)
date_now = str(datetime.datetime.now().date())
date_now = date_now.split("-")
date_now = '_'.join(date_now)
print("Đã tìm kiếm xong!")
print('Top 20 người điểm tương tác nhiều nhất là: ')
file = open('output.txt', 'w', encoding='utf-8')
file.write('Kết quả: ' + str(input_days) + ' - ' + str(datetime_now) + '\n')
file.write('Top 20 người điểm tương tác nhiều nhất là: \n')
for i in dict_final:
    r_name = requests.get(
        "https://graph.facebook.com/" + dict_final[i]['id'] + "?fields=name",
        params=payload).json()
    print(str(i) + '. ' + r_name['name'] + '(http://fb.com/' + str(dict_final[i]['id']) +') có tổng số điểm: ' + str(dict_final[i]['count']))
    file.write(str(i) + '. ' + r_name['name'] + '(http://fb.com/' + str(dict_final[i]['id']) +') có tổng số điểm: ' + str(dict_final[i]['count']) + '\n')
file.close()
print("Đã xuất kết quả ra file: output.txt")
