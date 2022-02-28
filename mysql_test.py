import mysql.connector
from dynaconf import settings

class WORD_POOL:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=settings['host'],
            user=settings['user'],
            password=settings['password'],
            database='mydatabase'
        )

    def get_rec(self):
        # print(mysql_connection)
        mycursor = self.mydb.cursor(dictionary=True)
        # curs.execute('CREATE DATABASE mydatabase')
        # curs.execute("CREATE TABLE customers (id VARCHAR(10), name VARCHAR(255))")
        # curs.execute("SHOW TABLES")

        # sql = "INSERT INTO customers (id, name) VALUES (%s, %s)"
        # val = ("1002", "suzuki")
        # mycursor.execute(sql, val)
        # self.mydb.commit()
        # print(mycursor.rowcount, "record inserted.")
        mycursor.execute("SELECT * FROM customers")
        myresult = mycursor.fetchall()
        # print(myresult)
        # for x in myresult:
        #     print(x)
        #     # print(type(x))
        mycursor.close()
        return myresult

if __name__ == '__main__':
    ins = WORD_POOL()
    res = ins.get_rec()
    print(res[1])


