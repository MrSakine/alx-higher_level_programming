#!/usr/bin/python3
"""
This module is about taking in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv[1:5]
    if len(args) == 4:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=args[0],
            password=args[1],
            database=args[2]
        )
        cur = db.cursor()
        cur.execute(
            "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(
                args[3])
        )
        print(cur.fetchone())
        cur.close()
        db.close()

