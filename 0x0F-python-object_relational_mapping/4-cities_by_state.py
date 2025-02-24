#!/usr/bin/python3
"""
list cities and states by joining the tables
usage: /4-cities_by_state.py <mysql username>
                             <mysql password>
                             <database name>

"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM `cities` LEFT JOIN `states` ON cities.state_id = states.id"
    )

    for row in cursor.fetchall():
        print(row)
