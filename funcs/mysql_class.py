#coding:utf8
import os
import sys
reload(sys)
from config.mysql_config import *
sys.setdefaultencoding("utf8")
import MySQLdb
class mysql_class(object):
    def __init__(self,config):
        try:
            self.conn = MySQLdb.connect(**config)
        except Exception as e:
            sys.exit("mysql config error{0}".format(e))

    def do_sql_with_result(self,sql,param=None):
        cur = self.conn.cursor()
        if param ==None:
            num = cur.execute(sql)
        elif isinstance(param.tuple):
            num = cur.execute(sql,param)
        else:
            sys.exit("sql语句参数类型错误")
        result = cur.fetchall()
        cur.close()
        return num,result

    def do_sql_without_result(self,sql,param=None):
        cur = self.conn.cursor()
        if param == None:
            try:
                cur.execute(sql)
                self.conn.commit()
            except Exception,e:
                print e
            else:
                return True
            finally:
                cur.close()
        elif isinstance(param,tuple):
            try:
                cur.execute(sql)
                self.conn.commit()
            except Exception,e:
                print e
            else:
                return True
            finally:
                cur.close()
        else:
            cur.close()
            sys.exit("sql语句参数类型错误")

    def get_all_tables(self):
        return self.do_sql_with_result("show tables")

    def get_tables_with_related(self,tables,related=None,need_fields="",wheres=""):
        '''
        查询关联表
        :example:d.get_tables_with_related(["sec_basic_info","sec_price_day"],[('a.sec_uni_code','b.sec_uni_code')],"a.*"," where a.sec_uni_code=1")
        :param t1:表一  默认a
        :param t2: 表二 默认b
        :param related: 关联条件[[('a.sec_uni_code','b.sec_uni_code'),('a.end_date','b.end_date')],[('a.com_uni_code','b.com_uni_code')]]
        :param need_fields:所需查询的字段
        :param wheres:where 条件限制
        :return:list
        '''
        if len(tables)==1:
            return self.do_sql_with_result("select {0} from {1} {2}".format(need_fields,tables[0], wheres))
        seq =['a','b','c','d','e']
        sql = " select  {0} from {1} a ".format(need_fields,tables[0])
        length = len(tables)
        for i in range(1,length):
            sql += " inner join " + tables[i]+" {0} on ".format(seq[i])+self.get_on_condition(related[i-1])
        sql +=wheres
        if (len(tables)-1)!=len(related):
            raise Exception("多表关联查询，参数不对等！")
        return self.do_sql_with_result(sql)

    def get_on_condition(self,params):
        if isinstance(params, tuple):
            return "=".join(params)
        else:
            string1 =list()
            for i in params:
                string1.append(self.get_on_condition(i))
            return " and ".join(string1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

if __name__ =="__main__":
    with mysql_class(dc) as d:
        print  d.get_tables_with_related(["sec_basic_info","sec_price_day"],[('a.sec_uni_code','b.sec_uni_code')],"a.*"," where a.sec_uni_code=1")
        print "-"*100
        print  d.get_tables_with_related(["sec_basic_info"], None,
                                         "*", " where sec_uni_code=1")