.. _cookbook_11:


菜谱 11：使用列表实现循环数据结构
====================================

在一些实际应用中，设计一个循环的数据结构是十分有利的。这里的循环数据结构指的是最后一个元素指向第一元素的结构。Python 内置的 list 能够很容易实现这个任务。::

	class Ring(object):

	    def __init__(self, l):
	        if not len(l):
	            raise "ring must have at least one element"
	        self._data = l

	    def __repr__(self):
	        return repr(self._data)

	    def __len__(self):
	        return len(self._data)

	    def __getitem__(self, i):
	        return self._data[i]

	    def turn(self):
	        last = self._data.pop(-1)
	        self._data.insert(0, last)

	    def first(self):
	        return self._data[0]

	    def last(self):
	        return self._data[-1]

使用这个结构的方式::

	>>> l = [{1:1}, {2:2}, {3:3}]
	>>> r = Ring(l)
	>>> r
	[{1: 1}, {2: 2}, {3: 3}]
	>>> r.first()
	{1: 1}
	>>> r.last()
	{3: 3}
	>>> r.turn()
	>>> r
	[{3: 3}, {1: 1}, {2: 2}]
	>>> r.turn()
	>>> r
	[{2: 2}, {3: 3}, {1: 1}]