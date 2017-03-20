import sqlite3
conn = sqlite3.connect('user.db')
c = conn.cursor()
if c.execute("DROP TABLE IF EXISTS userdata"):
    print("Done")
conn.commit()
conn.close()
# eCXboqv1&nQv


#2017-03-19T12:54:44.952481Z 1 [Note] A temporary password is generated for root@localhost: eCXboqv1&nQv

#ALTER user set password=PASSWORD("mysql123") where User='root';
