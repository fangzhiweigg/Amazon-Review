import time
import os
import random
import smtplib
import openpyxl
import socket
import socks
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def sendEmail(receiver_email,receiver_name):
    # 使用代理
    #ip, port = proxy.get_http_proxy()
    ip = '117.28.96.149'
    port = 9999
    socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, ip, port)
    socks.wrapmodule(smtplib)
    #socket.socket = socks.socksocket
    #发送者邮箱
    sender_email = '451284087@qq.com'
    #发送者邮箱密码
    passwd = 'impxoydkdevxbjae'
    #邮箱服务商
    host_server = 'smtp.qq.com'
    #消息
    message = """

<html><body><a>Hello World</a></body></html>

    """
    #标题
    title = '货代人必看的一封邮件'
    try:
        msg = MIMEMultipart('related')
        msgText = MIMEText(message, 'html', 'utf-8') #文本邮件
        msg.attach(msgText)
        msg['From'] = Header('witranscn@vip.163.com','utf-8')
        msg['To'] = Header(receiver_name,'utf-8')
        msg['Subject'] = Header(title, 'utf-8')
        server = smtplib.SMTP_SSL(host_server, 465)
        #server.starttls() # 调用starttls()方法，就创建了安全连接
        # server.set_debuglevel(1) # 记录详细信息
        server.login(sender_email, passwd) # 登录邮箱服务器
        server.sendmail(sender_email, receiver_email, msg.as_string()) # 发送信息
        server.quit()
        print("邮件:{}发送成功！".format(receiver_email))
    except Exception as e:
        print("邮件：{}发送失败：".format(receiver_email) + str(e))


sendEmail("451284087@qq.com", "kun.hk")
print("Done")