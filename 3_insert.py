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

        # insert

    def insert_user(self, userid, username, phone):
        query = "insert into user(userId,userName,phone)values({}, '{}', '{}')".format(userid, username, phone)

        print(query)
        cur = self.db.cursor()
        cur.execute(query)
        self.db.commit()
        print("user saved to db")


# main coding
helper = DBHelper()
helper.insert_user(1, "Siraz", "12431456")
helper.insert_user(2, "miraz", "1234556")
helper.insert_user(3, "faiyaz", "1234756")
helper.insert_user(4, "ritesh", "123746")