import sqlite3

def create_sqlite(dbname, tablename, tablecontent):
    # Create table
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    c.execute("CREATE TABLE  IF NOT EXISTS " + tablename + "(" + tablecontent + ")")

    conn.commit()
    conn.close()

def insert_sqlite(dbname, tablename, tablecontent):
    # Insert a row of data
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    c.execute("INSERT INTO " + tablename + " VALUES (" + tablecontent + ")")
    conn.commit()
    conn.close()

create_sqlite("user.db", "userdata", "username text, password text")
insert_sqlite("user.db", "userdata", "'raghunath','password'")