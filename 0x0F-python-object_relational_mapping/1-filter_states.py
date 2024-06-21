#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 a script that lists all states
 with a name starting with N (upper N)
 from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
