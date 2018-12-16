# -*- coding: UTF-8 -*-
import requests, json, facebook, datetime
import config
token = config.config_token
payload = {'method':'get','access_token':token}
graph=facebook.GraphAPI(token)
r_info = requests.get("https://graph.facebook.com/me?edges&access_token", params=payload).json()
print(r_info)
id = r_info['id']
name = r_info['name']
#---------------------------------------------------------------------
def info_birthday():
    try:
        birthday = r_info['birthday']
        if (len(birthday) == 5 ):
            temp = birthday[3:5]
            birthday = temp + birthday[2] + birthday[0:2]
        elif(len(birthday) == 10):
            temp = birthday[3:5]
            birthday = temp + birthday[2] + birthday[0:2] + birthday[5:10]
        else:
            birthday = ''
    except KeyError:
        birthday = ''
    return birthday
#---------------------------------------------------------------------
def info_zodiac():
    zodiac = ''
    try:
        if(len(info_birthday()) >= 5):
            if (int(info_birthday()[3:5]) == 3 and int(info_birthday()[0:2]) >= 21):
                zodiac = 'Bạch Dương'
            elif (int(info_birthday()[3:5]) == 4 and int(info_birthday()[0:2]) <=19):
                zodiac = 'Bạch Dương'

            if (int(info_birthday()[3:5]) == 4 and int(info_birthday()[0:2]) >= 20):
                zodiac = 'Kim Ngưu'
            elif (int(info_birthday()[3:5]) == 5 and int(info_birthday()[0:2]) <=20):
                zodiac = 'Kim Ngưu'

            if (int(info_birthday()[3:5]) == 5 and int(info_birthday()[0:2]) >= 21):
                zodiac = 'Song Tử'
            elif (int(info_birthday()[3:5]) == 6 and int(info_birthday()[0:2]) <=20):
                zodiac = 'Song Tử'

            if (int(info_birthday()[3:5]) == 6 and int(info_birthday()[0:2]) >= 21):
                zodiac = 'Cự Giải'
            elif (int(info_birthday()[3:5]) == 7 and int(info_birthday()[0:2]) <= 22):
                zodiac = 'Cự Giải'

            if (int(info_birthday()[3:5]) == 7 and int(info_birthday()[0:2]) >= 23):
                zodiac = 'Sư Tử'
            elif (int(info_birthday()[3:5]) == 8 and int(info_birthday()[0:2]) <= 22):
                zodiac = 'Sư Tử'

            if (int(info_birthday()[3:5]) == 8 and int(info_birthday()[0:2]) >= 23):
                zodiac = 'Xử Nữ'
            elif (int(info_birthday()[3:5]) == 9 and int(info_birthday()[0:2]) <= 22):
                zodiac = 'Xử Nữ'

            if (int(info_birthday()[3:5]) == 9 and int(info_birthday()[0:2]) >= 23):
                zodiac = 'Thiên Bình'
            elif (int(info_birthday()[3:5]) == 10 and int(info_birthday()[0:2]) <= 22):
                zodiac = 'Thiên Bình'

            if (int(info_birthday()[3:5]) == 10 and int(info_birthday()[0:2]) >= 23):
                zodiac = 'Thần Nông'
            elif (int(info_birthday()[3:5]) == 11 and int(info_birthday()[0:2]) <= 21):
                zodiac = 'Thần Nông'

            if (int(info_birthday()[3:5]) == 11 and int(info_birthday()[0:2]) >= 22):
                zodiac = 'Nhân Mã'
            elif (int(info_birthday()[3:5]) == 12 and int(info_birthday()[0:2]) <=21):
                zodiac = 'Nhân Mã'

            if (int(info_birthday()[3:5]) == 12 and int(info_birthday()[0:2]) >= 22):
                zodiac = 'Ma Kết'
            elif (int(info_birthday()[3:5]) == 1 and int(info_birthday()[0:2]) <=19):
                zodiac = 'Ma Kết'

            if (int(info_birthday()[3:5]) == 1 and int(info_birthday()[0:2]) >= 22):
                zodiac = 'Bảo Bình'
            elif (int(info_birthday()[3:5]) == 2 and int(info_birthday()[0:2]) <=18):
                zodiac = 'Bảo Bình'

            if (int(info_birthday()[3:5]) == 2 and int(info_birthday()[0:2]) >= 19):
                zodiac = 'Song Ngư'
            elif (int(info_birthday()[3:5]) == 3 and int(info_birthday()[0:2]) <=20):
                zodiac = 'Song Ngư'
    except:
        zodiac = ''
    return zodiac

# ---------------------------------------------------------------------
def info_age_range():
    now_year = datetime.datetime.now().year
    if (len(info_birthday()) == 10):
        birthday_year = int(info_birthday()[6:])
        age_range = now_year - birthday_year
    else:
        age_range = ''
    return str(age_range)
#---------------------------------------------------------------------
def info_education():
    try:
        # education = r_info['education']  # list
        education = ''
        for i in r_info['education']:
            name_school = i['school']['name']
            try:
                concentration_name = ' chuyên ngành: ' + i['concentration'][0]['name']
            except KeyError:
                concentration_name = ''
            type_school = i['type']
            if (type_school == 'High School'):
                type_school = 'Trường trung học'
            elif (type_school == 'College'):
                type_school = 'Trường đại học'
            education = education + type_school + ': ' + name_school + concentration_name + ' | '
    except KeyError:
        education = ''
    return education
#---------------------------------------------------------------------
def info_work():
    try:
        #work = r_info['work']  # list
        work = ''
        for i in r_info['work']:
            work_position = i['position']['name'] + ' tại: '
            work_employer = i['employer']['name']
            try:
                work_location = ' ở: ' + i['location']['name']
            except KeyError:
                work_location = ''
            work = work + work_position + work_employer + work_location + ' | '
    except KeyError:
        work = ''
    return  work
#---------------------------------------------------------------------
def info_mobile_phone():
    try:
        mobile_phone = r_info['mobile_phone']
    except KeyError:
        mobile_phone = ''
    return mobile_phone
#---------------------------------------------------------------------
def info_gender():
    try:
        gender = r_info['gender']
        if (gender == 'male'):
            gender = 'Nam'
        elif (gender == 'female'):
            gender = 'Nữ'
    except KeyError:
        gender = 'Không xác định'
    return gender
#---------------------------------------------------------------------
def info_interested_in():
    try:
        # interested_in = r_info['interested_in'] #list
        interested_in = ''
        for i in r_info['interested_in']:
            if (i == 'male'):
                i = 'Nam'
            elif (i == 'female'):
                i = 'Nữ'
            interested_in = interested_in + i + ' | '
    except KeyError:
        interested_in = ''
    return interested_in
#---------------------------------------------------------------------
def info_website():
    try:
        website = r_info['website']
    except KeyError:
        website = ''
    return website
#---------------------------------------------------------------------
def info_email():
    try:
        email = r_info['email']
    except KeyError:
        email = ''
    return email
#---------------------------------------------------------------------
def info_favorite_athletes():
    try:
        # favorite_athletes = r_info['favorite_athletes']  # list
        favorite_athletes = ''
        for i in r_info['favorite_athletes']:
            favorite_athletes = favorite_athletes + i['name'] + ' | '
    except KeyError:
        favorite_athletes = ''
    return favorite_athletes
#---------------------------------------------------------------------
def info_favorite_teams():
    try:
        # favorite_teams = r_info['favorite_teams']  # list
        favorite_teams = ''
        for i in r_info['favorite_teams']:
            favorite_teams = favorite_teams + i['name'] + ' | '
    except KeyError:
        favorite_teams = ''
    return favorite_teams
#---------------------------------------------------------------------
def info_sports():
    try:
        # sports = r_info['sports']  # list
        sports = ''
        for i in r_info['sports']:
            sports = sports + i['name'] + ' | '
    except KeyError:
        sports = ''
    return sports
#---------------------------------------------------------------------
def info_hometown():
    try:
        hometown = r_info['hometown']['name']  # page
    except KeyError:
        hometown = ''
    return hometown
#---------------------------------------------------------------------
def info_location():
    try:
        location = r_info['location']['name']  # page
    except KeyError:
        location = ''
    return  location
#---------------------------------------------------------------------
def info_locale():
    try:
        locale = r_info['locale']
    except KeyError:
        locale = ''
    return locale
#---------------------------------------------------------------------
def info_relationship_status():
    try:
        relationship_status = r_info['relationship_status']
        if (relationship_status == "It's complicated"):
            relationship_status = 'Phức tạp'
        elif (relationship_status == 'Single'):
            relationship_status = 'Độc thân'
        elif (relationship_status == 'In a civil union'):
            relationship_status = 'Kết hôn đồng tính'
        elif (relationship_status == 'In a relationship'):
            relationship_status = 'Hẹn hò'
        elif (relationship_status == 'Engaged'):
            relationship_status = 'Đã đính hôn'
        elif (relationship_status == 'Married'):
            relationship_status = 'Đã kết hôn'
        elif (relationship_status == 'In a domestic partnership'):
            relationship_status = 'Chung sống'
        elif (relationship_status == 'In an open relationship'):
            relationship_status = 'Tìm hiểu'
        elif (relationship_status == 'Separated'):
            relationship_status = 'Đã ly thân'
        elif (relationship_status == 'Đã ly hôn'):
            relationship_status = 'Hẹn hò'
        elif (relationship_status == 'Widowed'):
            relationship_status = 'Góa'
    except KeyError:
        relationship_status = ''
    return relationship_status
#---------------------------------------------------------------------
def info_bio():
    try:
        bio = r_info['bio']
    except KeyError:
        bio = ''
    return bio
#---------------------------------------------------------------------
def info_languages():
    try:
        # languages = r_info['languages'] #list
        languages = ''
        for i in r_info['languages']:
            languages = languages + i['name'] + ' | '
    except KeyError:
        languages = ''
    return languages
#---------------------------------------------------------------------
def info_political():
    try:
        political = r_info['political']
    except KeyError:
        political = ''
    return political
#---------------------------------------------------------------------
def info_religion():
    try:
        religion = r_info['religion']
    except KeyError:
        religion = ''
    return  religion
#---------------------------------------------------------------------
def info_quotes():
    try:
        quotes = r_info['quotes']
    except KeyError:
        quotes = ''
    return  quotes
#---------------------------------------------------------------------
print('Thông tin {} :'.format(name))
print('- Ngày sinh: ' + info_birthday())
print('- Tuổi: ' + info_age_range())
print('- Cung: ' + info_zodiac())
print('- Giới tính: ' + info_gender())
print('- Thích: ' + info_interested_in())
print('- Email: ' + info_email())
print('- Website: ' + info_website())
print('- Học vấn: ' + info_education())
print('- Công việc: '+ info_work())
print('- Mối quan hệ: ' + info_relationship_status())
print('- Ngôn ngữ: ' + info_languages())
print('- Chính trị: ' + info_political())
print('- Tôn giáo: ' + info_religion())
print('- Vận động viên yêu thích: ' + info_favorite_athletes())
print('- Hội thể thao yêu thích: ' + info_favorite_teams())
print('- Thể thao: ' + info_sports())
print('- Giới thiệu: ' + info_bio())
print('- Trích dẫn: ' + info_quotes())











