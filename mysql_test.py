from sqlite3 import DatabaseError
import mysql.connector
import settings

class WORD_POOL:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=settings.host,
            user=settings.user,
            password=settings.PD,
            database='yama_db'
        )
        self.curs = self.mydb.cursor(dictionary=True)
    def get_rec(self):
        # curs.execute('CREATE DATABASE mydatabase')
        # curs.execute("CREATE TABLE customers (id VARCHAR(10), name VARCHAR(255))")
        # curs.execute("SHOW TABLES")
        sql = "INSERT INTO customers (id, name) VALUES (%s, %s)"
        val = ("1001", "yamada")
        self.curs.execute(sql, val)
        self.mydb.commit()
        # print(curs.rowcount, "record inserted.")
        self.curs.execute("SELECT * FROM customers")
        # myresult = curs.fetchall()
        # print(myresult)
        # # for x in myresult:
        # #     print(x)
        # #     # print(type(x))
        # mycursor.close()
        # return myresult
    
    def create_table(self, tbl):
        # self.curs.execute("CREATE TABLE %s(id VARCHAR(10), name VARCHAR(12), age VARCHAR(3))"%(tbl))
        self.curs.execute("SHOW TABLES;")
        return self.curs.fetchall()


    def get_all_record(self):
        self.curs.execute("SELECT * FROM tbl")
        return self.curs.fetchall()

    def insert(self, id, name):
        sql = "INSERT INTO customers (id, name) VALUES (%s, %s)"
        val = (id, name)
        self.curs.execute(sql, val)
        self.mydb.commit()

    def del_data(self):
        sql = "DELETE from customers where id = '1010'"
        self.curs.execute(sql)

    def bulk_insert_and_update_users(self):

        data = [
            ['1001','test999', 10],
            ['1010','test998', 30]
        ]

        sql = 'INSERT INTO tbl (id, name, age) VALUES (%s, %s, %s) \
               ON DUPLICATE KEY UPDATE id = VALUES(id), name = VALUES(name)'
        

        self.curs.executemany(sql, data)
        self.mydb.commit()

    def bulk_update_and_update_users(self):

        data = [
            ['1001','test999', 10, '1001', 'test999'],
            ['1010','test998', 20, '1010', 'test998']
        ]

        sql = 'UPDATE tbl set id = %s, name = %s, age = %s \
               WHERE id = %s AND name = %s'
        
        self.curs.executemany(sql, data)
        self.mydb.commit()

    def original_update_elt(self):

        data = [
            ['1001','test999', 10],
            ['1010','test998', 20]
        ]

        sql = 'UPDATE tbl set ELT(id = %s, name = %s, age = %s\
               ON DUPLICATE KEY UPDATE id = VALUES(id), name = VALUES(name)'
        

        self.curs.executemany(sql, data)
        self.mydb.commit()


if __name__ == '__main__':
    cls = WORD_POOL()

    # res = cls.create_table('TBL')

    # print(res)

    # ins.insert('1003','satou')

    # print(ins.get_all_record())
    cls.bulk_insert_and_update_users()
    # cls.del_data()
    # cls.bulk_update_and_update_users()

    res = cls.get_all_record()
    print(res)


