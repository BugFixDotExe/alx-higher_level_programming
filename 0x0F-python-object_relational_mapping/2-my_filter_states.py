#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
  a script that takes in an argument and displays all values
  in the states table of hbtn_0e_0_usa where name matches the argument
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    search = sys.argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT MIN(id) as id,name\
            FROM states WHERE name LIKE '{}'\
            GROUP BY name".format(search))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
