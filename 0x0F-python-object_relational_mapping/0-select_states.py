#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This script is meant to fetch a database and query it for all it's items
in ascending order
"""
import MySQLdb
import sys

if __name__ == "__main__":
    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
