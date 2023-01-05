import mysql.connector as connector


class DBHelper:
    def __init__(self):
        self.db = connector.connect(host='localhost', port='3306',
                                    user='root',
                                    password='siraz',
                                    database='python')

        query = ('update user set age = 25 where userId = 2')

        print(query)
        cur = self.db.cursor()
        cur.execute(query)
        self.db.commit()
        print("updated")


# main coding
helper = DBHelper() 


