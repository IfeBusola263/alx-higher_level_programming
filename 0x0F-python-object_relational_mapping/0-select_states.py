#!/usr/bin/python3
'''
This module relates with a RDMS, with MySQLdb module.
'''

import MySQLdb
import sys

username = sys.argv[1]
pwd = sys.argv[2]
dBase = sys.argv[2]

dataBase = mySQLdb.connect(host='localhost:3306',
                           user=username, passwd=pwd, db=dBase)
cur = dataBase.cursor()
cur.execute("SELECT id, name FROM states ORDER BY id")
rows = cur.fetchall()

for row in rows:
    print(row)
