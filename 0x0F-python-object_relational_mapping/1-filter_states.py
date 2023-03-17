#!/usr/bin/python3
"""script that lists all states with a name starting with N"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    # conexión
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    # Para mostrar todos los registros en orden ascendente
    # pero solo los que empiezan con "N"
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1].startswith("N"):
            print(row)
    cur.close()
    conn.close()
