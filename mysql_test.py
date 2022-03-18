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
        curs.execute(sql, val)
        self.mydb.commit()
        # print(curs.rowcount, "record inserted.")
        curs.execute("SELECT * FROM customers")
        # myresult = curs.fetchall()
        # print(myresult)
        # # for x in myresult:
        # #     print(x)
        # #     # print(type(x))
        # mycursor.close()
        # return myresult
    
    def create_table(self, tbl):
        self.curs.execute("CREATE TABLE %s(id VARCHAR(10), age VARCHAR(3))"%(tbl))

    def get_all_record(self):
        self.curs.execute("SELECT * FROM customers")
        return self.curs.fetchall()

    def insert(self, id, name):
        sql = "INSERT INTO customers (id, name) VALUES (%s, %s)"
        val = (id, name)
        self.curs.execute(sql, val)
        self.mydb.commit()

if __name__ == '__main__':
    cls = WORD_POOL()

    cls.create_table('TBL')

    # ins.insert('1003','satou')

    # print(ins.get_all_record())

    # res = ins.get_rec()
    # print(res)


