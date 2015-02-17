.. _cookbook_5:


菜谱 5：发送带附件的邮件
===========================


我们平时需要使用 Python 发送各类邮件，这个需求怎么来实现？答案其实很简单，`smtplib <https://docs.python.org/2/library/smtplib.html>`_ 和 `email <https://docs.python.org/2/library/email.html>`_  库可以帮忙实现这个需求。`smtplib <https://docs.python.org/2/library/smtplib.html>`_ 和 `email <https://docs.python.org/2/library/email.html>`_ 的组合可以用来发送各类邮件：普通文本，HTML 形式，带附件，群发邮件，带图片的邮件等等。我们这里将会分几节把发送邮件功能解释完成。

`smtplib <https://docs.python.org/2/library/smtplib.html>`_ 是 Python 用来发送邮件的模块，`email <https://docs.python.org/2/library/email.html>`_ 是用来处理邮件消息。

发送带附件的邮件是利用 email.mime.multipart 的 MIMEMultipart 以及 email.mime.image 的 MIMEImage，重点是构造邮件头信息::

	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

	sender = '***'
	receiver = '***'
	subject = 'python email test'
	smtpserver = 'smtp.163.com'
	username = '***'
	password = '***'

	msgRoot = MIMEMultipart('mixed')
	msgRoot['Subject'] = 'test message'

	# 构造附件
	att = MIMEText(open('/Users/1.jpg', 'rb').read(), 'base64', 'utf-8')
	att["Content-Type"] = 'application/octet-stream'
	att["Content-Disposition"] = 'attachment; filename="1.jpg"'
	msgRoot.attach(att)

	smtp = smtplib.SMTP()
	smtp.connect(smtpserver)
	smtp.login(username, password)
	smtp.sendmail(sender, receiver, msgRoot.as_string())
	smtp.quit()


注意：这里的代码并没有把异常处理加入，需要读者自己处理异常。