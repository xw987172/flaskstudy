#coding:utf8
ENV = 'offline'
if ENV and ENV=='online':
    dc = {
        "host": '10.25.170.41',
        "port": 3306,
        "user": 'hs_dev',
        "passwd": 'UYLRPLLmiLMB3Gre',
        "db": 'data_center',
        "charset":"utf8",
    }
    qhqm = {
        "host": '10.252.218.51',
        "port": 3306,
        "user": 'qhqm',
        "passwd": 'ewB}1H^]|eXm52$T',
        "db": 'qhqm',
        "charset": "utf8",
    }
    product = {
        "host": '10.117.211.16',
        "port": 3306,
        "user": 'rreportor',
        "passwd": 'w3REW3432!lp',
        "db": 'qhqm',
        "charset": "utf8",
    }
elif ENV and ENV=='offline':
    dc = {
        "host": '114.55.108.136',
        "port": 3306,
        "user": 'dc_select',
        "passwd": 'Aenl1pnBtXWpQ5DW',
        "db": 'data_center',
        "charset": "utf8",
    }
    qhqm = {
        "host": '114.55.108.136',
        "port": 3306,
        "user": 'qhqm_select',
        "passwd": 'j-yl"?4T}u.xj>#W',
        "db": 'qhqm',
        "charset": "utf8",
    }
    product = {
        "host": '121.41.26.224',
        "port": 3306,
        "user": 'developments',
        "passwd": 'CgkJjQ4W1GeGO92s',
        "db": 'r_reportor',
        "charset": "utf8",
    }
else:
    raise Exception(u"环境变量ENV error！请赋予offline，online枚举值！")