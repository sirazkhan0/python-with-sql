import mysql.connector as connector


class DBHelper:
    def __init__(self):
        self.db = connector.connect(host='localhost', port='3306',
                                    user='root',
                                    password='siraz',
                                    database='python')

        query = 'create table if not exists user(userId int primary key,userName varchar(200),phone varchar(12))'

        cur = self.db.cursor()
        cur.execute(query)
        print("created")


# main coding
helper = DBHelper()
