import os
import psycopg2
from flask import Flask, render_template, request, redirect, session
from flask_session import Session
import hashlib

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
UPLOAD_FOLDER = './static/media/modalImages'
def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user="postgres",
                            password="ganesh99")
    return conn


@app.route('/')
def index():
    
    return render_template("index.html")

@app.route('/login' , methods =["GET", "POST"])
def loginPage():
    if request.method == "POST":
        uname = request.form.get("uname")
        passwd = request.form.get("passwd")
        session["name"] = request.form.get("uname")

        HashedPasswd = hashlib.md5(passwd.encode())
        prepared_statement_login = "SELECT * FROM login WHERE uname='{0}' AND passwd = '{1}';".format(uname, HashedPasswd.hexdigest())
        conn2 = get_db_connection()
        cur2 = conn2.cursor()

        cur2.execute('CREATE TABLE IF NOT EXISTS login (id serial PRIMARY KEY,'
                                 'uname varchar (150) NOT NULL,'
                                 'passwd varchar (150) NOT NULL);'
                                 )
        print(prepared_statement_login)
        cur2.execute(prepared_statement_login)
        user = cur2.fetchall()
        if(len(user) == 0):
            return render_template("loginError.html")

        cur2.close()
        conn2.close()
        return  render_template("index.html")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

@app.route("/tech-seg")
def techSeg():
    return render_template("tech-seg.html")

@app.route("/technology")
def technology():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS techcards (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'info varchar (150) NOT NULL);'
                                 )
    cur.close()
    conn.close()

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM techscards;')
    cards = cur.fetchall()
    print(cards)
    cur.close()
    conn.close()

    return render_template("technology2.html", cards = cards)

@app.route("/leadership")
def leadership():
    return render_template("leadership.html")


@app.route('/ai')
def ai():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM techscards;')
    cards = cur.fetchall()
    print(cards)
    cur.close()
    conn.close()
    return render_template("AIML.html", cards = cards)

@app.route('/cloud')
def cloud():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM techscards;')
    cards = cur.fetchall()
    print(cards)
    cur.close()
    conn.close()
    return render_template("cloud.html", cards = cards)

@app.route('/arvr')
def arvr():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM techscards;')
    cards = cur.fetchall()
    print(cards)
    cur.close()
    conn.close()
    return render_template("arvr.html", cards = cards)

@app.route('/datascience')
def datascience():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM techscards;')
    cards = cur.fetchall()
    print(cards)
    cur.close()
    conn.close()
    return render_template("datascience.html", cards = cards)

@app.route('/cybersec')
def cybersec():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM techscards;')
    cards = cur.fetchall()
    print(cards)
    cur.close()
    conn.close()
    return render_template("arvr.html", cards = cards)


@app.route('/3dprint')
def print3d():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM techscards;')
    cards = cur.fetchall()
    print(cards)
    cur.close()
    conn.close()
    return render_template("3dprint.html", cards = cards)

@app.route("/personality")
def personality():
    return render_template("personality.html")


@app.route("/admin-options")
def admin_Options():
    if not session.get("name"):
        return redirect("/login")
    return render_template("adminpage.html")

@app.route('/addcard', methods =["GET", "POST"])
def get_form_data():
    if request.method == "POST":
       file1 = request.files['file1']
       path = os.path.join(UPLOAD_FOLDER, file1.filename)
       file1.save(path)
       title = request.form.get("title")
       info = request.form.get("info")
       whatLearn = request.form.get("whatLearn")
       courseModules = request.form.get("courseModules")
       salFeatures = request.form.get("salFeatures")
       parentCourse = request.form.get("parentCourse")
       imageName = file1.filename
       domain = request.form.get("domain")
       hours = request.form.get("hours")
       email = request.form.get("email")
       contactName = request.form.get("contactname")
       contactNumber = request.form.get("contactnumber")

       prepared_statement = "INSERT INTO techscards (title, info, whatlearn, coursemodules, salfeatures, parentcourse, imagename, domain, hours, contactemail, contactperson, contactnumber) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}')".format(title, info, whatLearn, courseModules, salFeatures, parentCourse, imageName, domain, hours, email, contactName, contactNumber)
       conn = get_db_connection()
       cur = conn.cursor()
       cur.execute(prepared_statement)
       conn.commit()
       cur.close()
       conn.close()
       return render_template("adminpage.html")
    return render_template("form.html")

@app.route('/deletecard', methods = ["GET", "POST"])
def deletecard():
    if request.method == "POST":
       
        title = request.form.get("title")
        prepared_statement_delete = "DELETE FROM techscards WHERE (title = '{0}')".format(title)
        conn2 = get_db_connection()
        cur2 = conn2.cursor()
        print("delete")
        print(prepared_statement_delete)
        cur2.execute(prepared_statement_delete)
        conn2.commit()
        cur2.close()
        conn2.close()
        return  render_template("adminpage.html")
    return render_template("deleteform.html")

    @app.route('/aiMl')
    def aiMl():
        return render_template("AIML.html")






