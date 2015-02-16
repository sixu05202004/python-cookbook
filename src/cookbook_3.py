#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

sender = '***'
receiver = '***'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = '***'
password = '***'

msg = MIMEText(u"""<pre>
               <h1>你好</h1>
               </pre>""", 'html', 'utf - 8')

msg['Subject'] = subject

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
