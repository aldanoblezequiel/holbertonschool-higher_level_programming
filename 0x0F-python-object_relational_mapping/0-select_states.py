#!/usr/bin/python3
"""
This module that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Not execute mtf"""
    con_datab = MySQLdb.connect(host='localhost', user=argv[1],
                                password=argv[2], port=3306, database=argv[3])
    cursor = con_datab.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")
    elems = cursor.fetchall()

    for elem in elems:
        print(elem)
    con_datab.close()
