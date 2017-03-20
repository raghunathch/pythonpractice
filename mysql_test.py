import mysql.connector
import MySQLdb
import pymysql

hostname = 'localhost'
username = 'root'
password = 'mysql@123'
database = 'testdb'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT fname, lname, sex FROM employee" )

    for firstname, lastname, sex in cur.fetchall() :
        print firstname, lastname, sex


print "Using MySQLdb…"

myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

print "Using pymysql…"

myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

print "Using mysql.connector…"

myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()