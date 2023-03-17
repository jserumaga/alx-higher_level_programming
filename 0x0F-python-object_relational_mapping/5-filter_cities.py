#!/usr/bin/python3
"""script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    # conexión
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
    INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    cities = ''
    for row in query_rows:
        if row[2] == argv[4]:
            cities += '{}, '.format(row[1])
    print(cities[:-2])
    cur.close()
    conn.close()
