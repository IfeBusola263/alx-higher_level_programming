#!/usr/bin/python3
'''
This module relates with a RDMS, with MySQLdb module.
'''


if __name__ == '__main__':
    import MySQLdb
    import sys

    username = sys.argv[1]
    pwd = sys.argv[2]
    dBase = sys.argv[3]

    dataBase = MySQLdb.connect(host='localhost', port=3306,
                               user=username, passwd=pwd, db=dBase)
    cur = dataBase.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM \
    cities JOIN states ON cities.state_id = states.id \
    ORDER BY cities.id")

    rows = cur.fetchall()

    for row in rows:
        print(row)
