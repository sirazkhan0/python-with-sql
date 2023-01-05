# Importing module
import mysql.connector as connector

# Creating connection object
db = connector.connect(host='localhost', port='3306',
                        user='root',
                        password='siraz',
                        database='python')

# Printing the connection object                        

print(db)
