import mysql.connector
from mysql.connector import Error

class MySQLDB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
            print("Connected to MySQL.")
        except Error as e:
            print(f"Error: {e}")

    def execute_query(self, query: str, params: tuple = ()):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.cursor.fetchall()
        except Error as e:
            print(f"Query failed: {e}")
            return []

    def close(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()
            print("Connection closed.")


if __name__ == "__main__":
    db = MySQLDB(
    host='localhost',
    user='your_user',
    password='your_pass',
    database='your_db'
    )
    db.connect()

    rows = db.execute_query("SELECT name FROM Employee WHERE grade = %s", ('A',))
    for row in rows:
        print(row)

    db.close()
