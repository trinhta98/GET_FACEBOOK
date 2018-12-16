#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests, re, time
from connection import config
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
username = config.mail_username
password = config.mail_password

token = config.token
payload = {'method':'get', 'access_token':token}


def sendMailNow(userto, subject, content, user_name):
    print("Preparing message for sending mail to {}".format(user_name))
    msg = MIMEMultipart() #khai báo kiểu message
    msg['To'] = userto #người nhận, được nhiều đối tượng, ngăn cách nhau bởi dấu phẩy
    msg['Subject'] = subject #tiêu đề
    #thêm nội dung của mail vào (dưới dạng plain)
    msg.attach(MIMEText(content,'plain'))
    try:
        gmail = smtplib.SMTP('smtp.gmail.com:587')
        gmail.starttls()
        gmail.ehlo()
        gmail.login(username, password)
        print("Login successfully. Begin sending mail to {}".format(user_name))
        gmail.sendmail('chianhhieuem98hd@gmail.com', userto, msg.as_string()) # gửi mail với nội dung
        print("Yes, it' sent to {}".format(user_name))
    except:
        print("Không thể gửi đến địa chỉ email này !")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

post_id = '640651113003645'
op = []
list = ['androi', 'java', 'python', 'c', 'c++', 'php', 'c#']
def getComments():
    comments = requests.get("https://graph.facebook.com/" + post_id + "/comments",params=payload).json()
    for comment in comments['data']:
        user_name = comment['from']['name']
        user_id = comment['from']['id']
        message = comment['message']
        if user_id not in op:
            for item in list:
                if item in message.split(' '):
                    match = re.search(r"[\w._]+@\w+\.([A-Za-z]+\.)?[A-Za-z]{2,4}", message, re.I | re.U)
                    if match:  # nếu tồn tại chuỗi khớp
                        user_email = match.group()
                        print('{} lựa chọn ngôn ngữ: {} có địa chỉ email: {}'.format(user_name, item, user_email))
                        userto = user_email
                        subject = 'Hi ' + user_name + ' ! Đây là Email trả lời tự động theo yêu cầu comments'
                        content = 'Tài liệu/khóa học: ' + item
                        sendMailNow(userto, subject, content, user_name)
                        op.append(user_id)
                    break

if __name__ == '__main__':
    while True:
        getComments()
        time.sleep(10)