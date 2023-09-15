#!/usr/bin/python3
'''
This module querys from an SQL database, using the MySQLdb module.
'''


if __name__ == '__main__':
    import sys
    import MySQLdb

    username = sys.argv[1]
    pwd = sys.argv[2]
    dBase = sys.argv[3]
    name = sys.argv[4]

    # establish a connect with the database(SQL) using the API module(MySQLdb)
    dataBase = MySQLdb.connect(host='localhost', port=3306,
                               user=username, passwd=pwd, db=dBase)
    # create a cursor object to start the conversation
    # with the database
    cur = dataBase.cursor()

    cur.execute("SELECT cities.name \
    FROM cities \
    JOIN states ON cities.state_id = states.id \
    WHERE cities.state_id = ( SELECT id FROM states WHERE name = (%s)) \
    ORDER BY cities.id", (name,))

    rows = cur.fetchall()

    flag = 0
    for row in rows:

        for col in row:
            if flag == 1:
                print(', ', end='')
            print(col, end='')
            flag = 1

    print()
