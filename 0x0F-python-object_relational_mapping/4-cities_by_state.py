#!/usr/bin/python3
"""
This module is about listing all cities from the database hbtn_0e_4_usa
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
        cur.execute(
            """
            SELECT cities.id, cities.name, states.name FROM cities
            INNER JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id ASC
            """
        )
        for data in cur.fetchall():
            print(data)
        cur.close()
        db.close()
