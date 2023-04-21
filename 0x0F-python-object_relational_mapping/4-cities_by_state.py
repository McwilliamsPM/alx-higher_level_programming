#!/usr/bin/python3
""" a script that list all citites in database hbtn_0e_4_usa
"""

import sys
import MySQLdb

    username = sys.argv[1], password = sys.argv[2], db_name = sys.argv[3], state_searched = sys.argv[4], host = 'localhost', port = 3306
        db = MySQLdb.connect(host=host, user=username, passwd=password, db=db_name, port=port)
        cur = db.cursor()
        cur.execute("SELECT cities id, cities name,"
            "states.name FROM cities LEFT JOIN states ON "
            "states.id = cities.state_id ORDER BY cities.id ASC")

        result = cur.fetchall()
        cur.close()
        db.close()


        for row in result:
            print(row)
