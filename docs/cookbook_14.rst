.. _cookbook_14:


菜谱 14：从.zip文件中读取数据
==============================

Python 能够直接读取 zip 文件中的数据。我们现在需要实现这样一个小任务：直接读取一个 zip 文件，获取里面包含的文件列表以及每个文件的大小。

Python 的 zipfile 模块可以轻松地帮助我们解决这个任务::

	import zipfile

	z = zipfile.ZipFile("test.zip", "r")
	for filename in z.namelist():
	        print filename
	        bytes = z.read(filename)
	        print len(bytes)

这里需要注意地是 zipfile 模块有些 zip 文件是无法处理，具体是里面插入了注释的 zip 文件或者多分卷的 zip 文件。