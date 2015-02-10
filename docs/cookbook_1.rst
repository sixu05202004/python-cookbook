.. _cookbook_1:


菜谱1：创建一个唯一的 session ID
==================================

在网站开发的时候，常常需要生成一个唯一的的会话（session）id，这个会话 id 存储在 cookie 中或者在其它安全的地方。::

	# create a unique session id
	# input - string to use as part of the data used to create the session key.
	#         Although not required, it is best if this includes some unique 
	#         data from the site, such as it's IP address or other environment 
	#         information.  For ZOPE applications, pass in the entire ZOPE "REQUEST"
	#         object.
	def makeSessionId(st):
		import md5, time, base64, string
		m = md5.new()
		m.update('this is a test of the emergency broadcasting system')
		m.update(str(time.time()))
		m.update(str(st))
		return string.replace(base64.encodestring(m.digest())[:-3], '/', '$')

	def makeSessionId_nostring(st):
		import md5, time, base64
		m = md5.new()
		m.update('this is a test of the emergency broadcasting system')
		m.update(str(time.time()))
		m.update(str(st))
		return base64.encodestring(m.digest())[:-3].replace('/', '$')


输入参数：st，不限制 st 唯一，但是建议传入的 st 是唯一的，可以是 IP 或者一些环境信息。
输出：唯一的 session id 字符串。