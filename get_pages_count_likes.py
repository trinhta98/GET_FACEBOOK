# -*- coding: UTF-8 -*-
import requests
import config

token = 'EAAAAAYsX7TsBACc7x93hd9hh4QoDK2K3oDUZCeb8XiOb7OjWQxlyh2vlP7Sy7Dh13ZA7zMOoYhOgIPHTZBnYPP2THcH7a6a9QLGJYZB1lFxhbph9ZAFIvIlBxWRjhsssCNnP0Hhq2qkKWRfdEiO5gUmzfZBijLTGmrNbZCPvVGUjFR6hfAMZC3QkHH88s7kI1Itq1tA27ahEC0l0s4lovZBlU'
payload = {'method':'get','access_token':token}
payload2 = {'method':'delete','access_token':token}
user_id = '100008195284583'

r_likes = requests.get("https://graph.facebook.com/" + user_id + "?fields=likes.summary(true)&access_token", params=payload).json()
total_count = r_likes['likes']['summary']['total_count']
print('Tổng số pages đã từng like là: {}'.format(total_count))
count = 1
for i in r_likes['likes']['data']:
    name = i['name']
    id = i['id']
    print(str(count) + '. Đã like page: {} có id: {}'.format(name, id))
    # lc = 0
    # lc = input('-->Bạn có muốn unlike page này không?(y/n): ')
    # if (lc == 'y'):
    #     r2 = testrequests.get("https://graph.facebook.com/" + id + "/likes", params=payload2).json()
    #     if (r2 == True):
    #         print('-->Bạn đã unlike page này thành công !')
    #     else:
    #         print('-->Không unlike được rồi :(( hiu hiu')
    count += 1
try:
    paging = r_likes['likes']['paging']['next']
except KeyError:
    print('Người này để chế độ riêng tư !')
    exit()
for j in range(0, int(total_count)//100):
    try:
        r = requests.get(paging).json()
        for i in r['data']:
            name = i['name']
            id = i['id']
            print(str(count) + '. Đã like page: {} có id: {}'.format(name, id))
            # lc = 0
            # lc = input('-->Bạn có muốn unlike page này không?(y/n): ')
            # if(lc == 'y'):
            #     r2 = testrequests.get("https://graph.facebook.com/" + id + "/likes", params=payload2).json()
            #     if(r2 == True):
            #         print('-->Bạn đã unlike page này thành công !')
            #     else:
            #         print('-->Không unlike được rồi :(( hiu hiu')
            count += 1
        paging = r_likes['paging']['next']
    except KeyError:
        print('Tổng số pages vẫng đang like: {}'.format(int(count - 1)))
        print('Tổng số pages đã unlike hoặc folow: {}'.format(str(total_count - count + 1)))
        exit()

