.. _cookbook_9:


菜谱 9：soundex 算法
=====================

SOUNDEX 返回由四个字符组成的代码 (SOUNDEX) 以评估两个字符串的相似性。返回的第一个字符是输入字符串的第一个字符，返回的第二个字符到第四个字符是数字。

soundex 代码如下::

	def soundex(name, len=4):
	    """ soundex module conforming to Knuth's algorithm
	        implementation 2000-12-24 by Gregory Jorgensen
	        public domain
	    """

	    # digits holds the soundex values for the alphabet
	    digits = '01230120022455012623010202'
	    sndx = ''
	    fc = ''

	    # translate alpha chars in name to soundex digits
	    for c in name.upper():
	        if c.isalpha():
	            if not fc:
	                fc = c   # remember first letter
	            d = digits[ord(c) - ord('A')]
	            # duplicate consecutive soundex digits are skipped
	            if not sndx or (d != sndx[-1]):
	                sndx += d
	    print sndx

	    # replace first digit with first alpha character
	    sndx = fc + sndx[1:]

	    # remove all 0s from the soundex code
	    sndx = sndx.replace('0', '')

	    # return soundex code padded to len characters
	    return (sndx + (len * '0'))[:len]

需要注意的是代码设计为处理英文名称。