#!/usr/bin/python3
"""Lists states with a name starting with N from the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create cursor
    cur = db.cursor()

    # Execute query
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")

    # Fetch all rows
    rows = cur.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
