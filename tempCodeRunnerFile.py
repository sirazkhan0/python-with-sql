import mysql.connector as connector


class DBHelper:
    def __init__(self):
        self.db = connector.connect(host='localhost', port='3306',
                                    user='root',
                                    password='siraz',
                                    database='python')

        query = ('alter table user add column age int (20)')

        print(query)
        cur = self.db.cursor()
        cur.execute(query)
        self.db.commit()
        print("create new column")


# main coding
helper = DBHelper() 


