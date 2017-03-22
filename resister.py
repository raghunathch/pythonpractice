
from bottle import get, post, request, Bottle, run, route
import mysql.connector
import MySQLdb
import pymysql

hostname = 'localhost'
dbuname = 'root'
dbpasswd = 'mysql@123'
database = 'testdb'

def doQuery(conn, fname, lname, sex, uname, passwd):
    cur = conn.cursor()
    #insrt = "INSERT INTO employee (fname, lname, sex, uname, password) VALUES ('%s', '%s', '%s', '%s', '%s');"%(fname, lname, sex, uname, passwd)
    cur.execute("INSERT INTO employee (fname, lname, sex, uname, password) VALUES ('%s', '%s', '%s', '%s', '%s');"%(fname, lname, sex, uname, passwd))
    cur.execute( "SELECT fname, lname, sex, uname FROM employee" )

    for firstname, lastname, sex, uname in cur.fetchall():
        print firstname, lastname, sex, uname

def register_user(fname, lname, sex, uname, passwd):
    myConnection = pymysql.connect( host=hostname, user=dbuname, passwd=dbpasswd, db=database)
    doQuery(myConnection, fname, lname, sex, uname, passwd)
    myConnection.close()

@get('/register') # or @route('/register')
def register():
    return '''
        <center>
        <form action="/register" method="post"><br><br>
            <br><br>Please enter the details to register to the portal <br><br>
            Firstname: <input name="fname" type="text" /><br>
            Lastname: <input name="lname" type="text" /><br>
            Sex: <input sex="sex" type="text" /><br>
            Username: <input name="uname" type="text" /><br>
            Password: <input name="passwd" type="password" /><br>
            <input value="Reset Form" type="reset" /><br>
            <input value="Submit Form" type="submit" />
        </form>
        </center>
    '''

@post('/register') #, method='POST') # or @route('/register', method='POST')
def do_register():
    fname = request.forms.get('fname')
    lname = request.forms.get('lname')
    sex = request.forms.get('sex')
    uname = request.forms.get('uname')
    passwd = request.forms.get('passwd')
    register_user(fname, lname, sex, uname, passwd)
    #if register_user(fname, lname, sex, uname, passwd):
    #    return "<p>Your login information registered.</p>"
    #else:
    #    return "<p>Registration failed.</p>"

run(host='localhost', port=8080, debug=True)