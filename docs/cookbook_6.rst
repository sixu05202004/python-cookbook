.. _cookbook_6:


菜谱 6：群发邮件
===========================


我们平时需要使用 Python 发送各类邮件，这个需求怎么来实现？答案其实很简单，`smtplib <https://docs.python.org/2/library/smtplib.html>`_ 和 `email <https://docs.python.org/2/library/email.html>`_  库可以帮忙实现这个需求。`smtplib <https://docs.python.org/2/library/smtplib.html>`_ 和 `email <https://docs.python.org/2/library/email.html>`_ 的组合可以用来发送各类邮件：普通文本，HTML 形式，带附件，群发邮件，带图片的邮件等等。我们这里将会分几节把发送邮件功能解释完成。

`smtplib <https://docs.python.org/2/library/smtplib.html>`_ 是 Python 用来发送邮件的模块，`email <https://docs.python.org/2/library/email.html>`_ 是用来处理邮件消息。

群发邮件的时候需要注意收件人（receiver）的值，它为列表形式::

	import smtplib
	from email.mime.text import MIMEText

	sender = '***'
	receiver = ['***', '***', '...', '***']
	subject = 'python email test'
	smtpserver = 'smtp.163.com'
	username = '***'
	password = '***'

	msg = MIMEText('你好', 'plain', 'utf-8')

	msg['Subject'] = subject

	smtp = smtplib.SMTP()
	smtp.connect(smtpserver)
	smtp.login(username, password)
	smtp.sendmail(sender, receiver, msg.as_string())
	smtp.quit()


注意：这里的代码并没有把异常处理加入，需要读者自己处理异常。