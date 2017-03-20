from bottle import get, post, request, Bottle, run, route
import mysql.connector
import MySQLdb
import pymysql


@get('/login') # or @route('/login')
def login():
    return '''
        <center>
        <form action="/login" method="post"><br><br>
            <br><br>Please enter your credentials to access the portal <br><br>
            Username: <input name="username" type="text" /><br>
            Password: <input name="password" type="password" /><br>
            <input value="Reset Form" type="reset" />
            <input value="Login" type="submit" />
        </form>
        <form action="/register" method="post"><br><br>
            <input value="Register" type="submit" />
        </form>
        <form action="/login" method="post"><br><br>
            <input value="Forget Password" type="submit" />
        </form>
        </center>
    '''
        #<button type="button">Forgot Password</button>
        #<button type="submit" formaction="/register">Sign Up</button>


@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


def check_login(username, password):
    if username == "raghunath" and password == "password":
        return True
    else:
        return False


#Registration Script as below

#fname = ""
#lname = ""
#sex = ""
#uname = ""
#passwd = ""

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

@post('/register') # or @route('/register', method='POST')
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

hostname = 'localhost'
dbuname = 'root'
dbpasswd = 'mysql@123'
database = 'testdb'

def register_user(fname, lname, sex, uname, passwd) :
    myConnection = pymysql.connect( host=hostname, user=dbuname, passwd=dbpasswd, db=database )
    #doQuery( myConnection, fname, lname, sex, uname, passwd )
    myConnection.close()


def doQuery( conn , fname, lname, sex, uname, passwd) :
    cur = conn.cursor()

    cur.execute("INSERT INTO employee (fname, lname, sex, uname, password) VALUES ("+ fname + ", " + lname + ", " + sex + ", " + uname + ", " + passwd + ")")
    cur.execute( "SELECT fname, lname, sex, uname, passwd FROM employee" )

    for firstname, lastname, sex in cur.fetchall() :
        print firstname, lastname, sex

run(host='localhost', port=8080, debug=True)