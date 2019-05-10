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
    def test_buy(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    test = unittest.TestSuite()
    test.addTest(ECShop('test_ECshop'))
    test.addTest(ECShop('test_buy'))
    rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
    file_path = os.path.abspath('.')+'/report/'+rq+'-result.html'
    file_result = open(file_path,'wb')
    runner=common.HTMLTestRunner.HTMLTestRunner(
        stream=file_result,title=u'ECshop测试报告',description = u"用例执行情况")
    runner.run(test)
    file_result.close()