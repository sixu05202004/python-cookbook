.. _cookbook_12:


菜谱 12：使用 UDP 数据包发送消息
=======================================

使用 UDP 数据包发送短的文本消息实现是很简单的并且提供可一个非常轻量级的消息传递通道。但是这种模式有很大的缺陷，就是不保证的数据的可靠性，有可能会存在丢包的情况，甚至严重的情况就是服务器不可用的时候，会完全丢失你的消息。不过这个任务会在有些情况下十分有作用：

	* 你不关心消息是否丢失；
	* 你不想要终止程序只是因为消息无法传递；

::

	# server.py
	import socket
	port = 8081
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(("", port))
	print "waiting on port:", port
	while 1:
	    data, addr = s.recvfrom(1024)
	    print data

	---

	# client.py
	import socket
	port = 8081
	host = "localhost"
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(("", 0))
	s.sendto("Holy Guido! It's working.", (host, port))


还有一个提醒事项，不要用上面的程序发送大量的数据包，尤其是在 Windows 上。要是想要发送大的消息的话，你可以这样做::

	BUFSIZE = 1024
	while msg:
	    s.sendto(msg[:BUFSIZE], (host, port))
	    msg = msg[BUFSIZE:]