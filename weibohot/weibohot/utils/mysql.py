import pymysql

from weibohot.utils.configparser import MyConfigParser


class MysqlUtil:

    def __init__(self):
        self.myConfigParser = MyConfigParser()
        self.mysqlCfFileName = 'mysql'
        self.conn = pymysql.Connection

    def init_mysql(self):
        mysqlCf = self.myConfigParser.getCfByFileName(self.mysqlCfFileName)
        self.conn = pymysql.connect(host=mysqlCf.get('mysql', 'host'), port=int(mysqlCf.get('mysql', 'port')),
                                    user=mysqlCf.get('mysql', 'user'), passwd=mysqlCf.get('mysql', 'passwd'),
                                    db=mysqlCf.get('mysql', 'db'), charset=mysqlCf.get('mysql', 'charset'))

        return self.conn

    def close_mysql(self):
        self.conn.close()

    def insertHotRecord(self, item):
        self.init_mysql()
        cursor = self.conn.cursor()
        insert_sql = 'insert hot_record_dev(temp_index,title,hit,type,date,href) values (%s, %s, %s, %s, now(),%s)'
        cursor.execute(insert_sql, (item.get('index'), item.get('title'), item.get('hit'), item.get('type'), item.get('hot_href')))
        self.conn.commit()
        self.conn.close()


