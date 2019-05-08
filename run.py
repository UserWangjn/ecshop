from script.module import *
import time
import os.path
import unittest
import common.HTMLTestRunner
class ECShop(unittest.TestCase):
    def setUp(self):
        pass

    def test_ECshop(self):
        tspath = os.path.abspath('.')
        tsname = tspath+'/data/testsuite.xlsx'
        self.assertTrue(read_testsuite(tsname))

    def tearDown(self):
        pass

if __name__ == '__main__':
    test = unittest.TestSuite()