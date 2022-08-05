#!/usr/bin/python3
"""Listing cities from the Dbase
"""
from sqlite3 import connect
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities LEFT JOIN states "
                "ON cities.state_id = states.id "
                "WHERE states.name = %s ORDER BY "
                "cities.id ASC", (argv[4],))

    query_rows = cur.fetchall()

    s = []
    for row in query_rows:
        s.append(row[1])
    print(", ".join(s))
    cur.close()
    db.close()
