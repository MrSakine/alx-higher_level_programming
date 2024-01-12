#!/usr/bin/python3
"""
This module is about taking in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
& sql injection free
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
        """
        SELECT * FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        WHERE states.name='{}' ORDER BY cities.id ASC""".format(
            name)
    )
    data = cur.fetchall()
    i = 0
    for d in data:
        if (i > 0):
            print(", ", end="")
        print(d[2], end="")
        i += 1
    print()
    cur.close()
    db.close()
