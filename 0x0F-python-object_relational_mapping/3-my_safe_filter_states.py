#!/usr/bin/python3
""" a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. One of it mus be safe from SQL injections
"""

import sys
import MySQLdb

if __name__ == '__main__':
    list_it()

    username = sys.argv[1], password = sys.argv[2], db_name = sys.argv[3], state_searched = sys.argv[4], host = 'localhost', port = 3306
    db = MySQLdb.connect(host=host, user=username, passwd=password, db=db_name, port=port)

        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name = %s"
                " ORDER BY id ASC".format(state_searched))

      result = cur.fetchall()
   cur.close()
    db.close()

        for row in result:
            print(row)

