#coding:utf8
import os
import sys
reload(sys)
sys.setdefaultencoding("utf8")
class BaseException(Exception):
    def __init__(self,error):
        super(BaseException, self).__init__()
        self.err = error
