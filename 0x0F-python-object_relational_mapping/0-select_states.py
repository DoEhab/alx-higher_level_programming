#!/usr/bin/python3
#list all states

import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost",
                        port=3306,
                        user=username,
                        passwd=password,
                        db=database)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY id ASC ")

    [print(state) for state in cursor.fetchall()]