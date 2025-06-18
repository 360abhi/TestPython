import sqlite3
from typing import Optional

class SqliteDB:

    def __init__(self,db_path:str):
        """Initialize Connection"""
        self.db_path = db_path
        self.conn:Optional[sqlite3.Connection] = None
        self.cursor:Optional[sqlite3.Cursor] = None

    def connect(self):
        """Connect to the Database """
        try:
            self.conn = sqlite3.connect(database=self.db_path)
            self.cursor  = self.conn.cursor()
            print("Connected to the sqlite3 Database")
        except sqlite3.Error as e:
            print(f"Error connecting to the sqlite databse {str(e)}")

    def execute_query(self,query:str,params:tuple=()):
        """Run Sql query with optional parameters"""
        try:
            self.cursor.execute(query,params)
            self.conn.commit()
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error executing the query {str(e)}")

    def close(self):
        """Close the connection"""
        if self.conn:
            self.conn.close()
            print("Connection closed")


if  __name__ == "__main__":
    db = SqliteDB("DB/employee.db")
    db.connect()

    results = db.execute_query("SELECT * FROM Employee WHERE grade = ?", ('A',))
    for row in results:
        print(row)

    db.close()

        
        