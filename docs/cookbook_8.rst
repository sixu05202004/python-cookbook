.. _cookbook_8:


菜谱 8：支持简单命令行
==================================

本任务最初的目的只是为了在测试过程中使用简单的命令行运行不同的函数，类似运行 “python test_test.py” 运行整个测试，运行 “python test_test.py debug” 来运行测试但是不收集运行结果，请看如下的代码::

	import unittest
	import sys


	class Tests(unittest.TestCase):

	    def testAddOnePlusOne(self):
	        assert 1 == 2


	def main():
	    unittest.TextTestRunner().run(test_suite())


	def test_suite():
	    return unittest.makeSuite(Tests, 'test')


	def debug():
	    test_suite().debug()

	if __name__ == '__main__':

	    if len(sys.argv) > 1:
	        globals()[sys.argv[1]]()
	    else:
	        main()

这里如果在命令行中直接运行 “python cookbook_8.py” 就会执行 “main()”；如果在命令行中运行 “python cookbook_8.py debug” 会执行 “debug()”。

“globals()” 返回的是当前全局变量的引用。如果有其它的需求，可以充分利用本任务来延伸！


