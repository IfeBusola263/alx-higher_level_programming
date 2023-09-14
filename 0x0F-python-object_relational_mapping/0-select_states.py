#!/usr/bin/python3
'''
This module relates with a RDMS, with MySQLdb module.
'''

import MySQLdb
import sys

username = sys.argv[1]
pwd = sys.argv[2]
dBase = sys.argv[3]

dataBase = MySQLdb.connect(host='localhost', port=3306,
                           user=username, passwd=pwd, db=dBase)
cur = dataBase.cursor()
cur.execute("SELECT id, name FROM states ORDER BY id")
rows = cur.fetchall()

for row in rows:
    print(row)
