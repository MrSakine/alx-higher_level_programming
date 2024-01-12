#!/usr/bin/python3
"""
This module is about listing all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv[1:4]
    if len(args) == 3:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=args[0],
            password=args[1],
            database=args[2]
        )
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY states.id ASC")
        for data in cur.fetchall():
            print(data)
        cur.close()
        db.close()
