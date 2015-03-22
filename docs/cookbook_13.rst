.. _cookbook_13:


菜谱 13：在文件中搜索以及替换文本
=====================================

使用命令行简单地替换一个文件中的文本内容，并且生成一个新的自定义文件名的文件。这是我们平时工作中常见的一个小任务，下面的这一段小代码能够轻松地完成这个任务::

	import os
	import sys
	usage = "usage: %s search_text replace_text [infilename [outfilename]]" % os.path.basename(
	    sys.argv[0])

	if len(sys.argv) < 3:
	    print usage

	else:
	    stext = sys.argv[1]
	    rtext = sys.argv[2]
	    print "There are %s args " % len(sys.argv)

	    if len(sys.argv) > 4:
	        input = open(sys.argv[3])
	        output = open(sys.argv[4], 'w')

	        for s in input:
	            output.write(s.replace(stext, rtext))

	        input.close()
	        output.close()

当我们使用 "python cookbook_13.py 1 a test.txt new.txt" 命令行的时候，test.txt 中 1 会被替换成 a，并且替换后的内容写入到 new.txt 中。

注意：infilename，outfilename 这两个参数没有的话，程序并不会报错，但是会输出类似 “There are ...” 的语句。如果命令行参数小于 3 的话，会输出 “usage:。。。”。