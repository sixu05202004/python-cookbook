#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
