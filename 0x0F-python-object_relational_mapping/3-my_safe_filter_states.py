#!/usr/bin/python3
"""
This module is about taking in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument &
safe from MySQL injections
"""
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv[1:]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=args[0],
        password=args[1],
        database=args[2]
    )
    cur = db.cursor()
    name = (
        args[3][:args[3].find(";")].strip("'") if ";" in args[3] else args[3]
    )
    cur.execute(
        "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(
            name)
    )
    print(cur.fetchone())
    cur.close()
    db.close()
