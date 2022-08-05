#!/usr/bin/python3
"""Modulus listing states from DB
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY \
                '{}' ORDER BY id ASC"
                .format(argv[4]))

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
