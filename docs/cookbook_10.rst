.. _cookbook_10:


菜谱 10：统计单词出现的频率
===========================

平时我们在工作的时候需要统计一篇文章或者网页出现频率最高的单词，或者需要统计单词出现频率排序。那么如何完成这个任务了？

例如，我们输入的语句是 “Hello there this is a test.  Hello there this was a test, but now it is not."，希望得到的升序的结果::

	[[1, 'but'], [1, 'it'], [1, 'not.'], [1, 'now'], [1, 'test,'], [1, 'test.'], [1, 'was'], [2, 'Hello'], [2, 'a'], [2, 'is'], [2, 'there'], [2, 'this']]

得到降序的结果是::

	[[2, 'this'], [2, 'there'], [2, 'is'], [2, 'a'], [2, 'Hello'], [1, 'was'], [1, 'test.'], [1, 'test,'], [1, 'now'], [1, 'not.'], [1, 'it'], [1, 'but']]

完成这个结果的代码如下::

	class Counter(object):

	    def __init__(self):
	        self.dict = {}

	    def add(self, item):
	        count = self.dict.setdefault(item, 0)
	        self.dict[item] = count + 1

	    def counts(self, desc=None):
	        result = [[val, key] for (key, val) in self.dict.items()]
	        result.sort()
	        if desc:
	            result.reverse()
	        return result

	if __name__ == '__main__':

	    '''Produces:

	        >>> Ascending count:
	        [[1, 'but'], [1, 'it'], [1, 'not.'], [1, 'now'], [1, 'test,'], [1, 'test.'], [1, 'was'], [2, 'Hello'], [2, 'a'], [2, 'is'], [2, 'there'], [2, 'this']]
	        Descending count:
	        [[2, 'this'], [2, 'there'], [2, 'is'], [2, 'a'], [2, 'Hello'], [1, 'was'], [1, 'test.'], [1, 'test,'], [1, 'now'], [1, 'not.'], [1, 'it'], [1, 'but']]
	    '''

	    sentence = "Hello there this is a test.  Hello there this was a test, but now it is not."
	    words = sentence.split()
	    c = Counter()
	    for word in words:
	        c.add(word)
	    print "Ascending count:"
	    print c.counts()
	    print "Descending count:"
	    print c.counts(1)