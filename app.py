from urllib.parse import urlparse

import MySQLdb
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL

from chat import get_response

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'praveen'
app.config['MYSQL_PASSWORD'] = 'praveen'
app.config['MYSQL_DB'] = 'breakdown'


mysql = MySQL(app)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/login')
def login():  # put application's code here
    return render_template('login.html')


@app.route('/location')
def location():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from location")
    data = cur.fetchall()
    cur.close()
    return render_template('Locationlist.html', place=data)


@app.route('/logincheck', methods=['POST', 'GET'])
def logincheck():
    if request.method == "POST":
        name = request.form['uname']
        psw = request.form['psw']

    if name=="admin":
        cur = mysql.connection.cursor()
        query = "SELECT * from signup where username=%s and password = %s"
        vals = (name, psw,)
        cur.execute(query, vals)
        data = cur.fetchall()
        cur.close()
        if len(data)>0:
             cur = mysql.connection.cursor()
             cur.execute("SELECT * from mechanic,location where mechanic.wloc=location.lid")
             mechdata = cur.fetchall()
             cur.close()

             cur = mysql.connection.cursor()
             cur.execute("SELECT * from location")
             mecharea = cur.fetchall()
             cur.close()
             return render_template('Locationlist.html', mech=mechdata, mechloc=mecharea, userdet=data)
        else:
             return ("invalid login")

    else:
        cur = mysql.connection.cursor()
        query="SELECT * from signup where username=%s and password = %s"
        vals=(name,psw,)
        cur.execute(query,vals)
        data = cur.fetchall()
        cur.close()

        if len(data) > 0:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * from mechanic,location where mechanic.wloc=location.lid")
            mechdata = cur.fetchall()
            cur.close()

            cur = mysql.connection.cursor()
            cur.execute("SELECT * from location")
            mecharea = cur.fetchall()
            cur.close()
            return render_template('userareawisemechaniclist.html',  mech=mechdata, mechloc=mecharea, userdet=data)
        else:
             return ("invalid login")


@app.route('/logincheck1', methods=['POST', 'GET'])
def logincheck1():
    if request.method == "POST":
        name = request.form['uname']
        psw = request.form['psw']

        cur = mysql.connection.cursor()
        query = "SELECT * from signup where username=%s and password = %s"
        vals = (name, psw,)
        cur.execute(query, vals)
        dataval = cur.fetchall()
        cur.close()
        if len(dataval)>0:
            return str(("Total rows are", len(dataval)))
        else:
            return ("Not valid")


@app.route('/mechanic')
def mechanic():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from mechanic,location where mechanic.wloc=location.lid")
    mechdata = cur.fetchall()
    cur.close()
    return render_template('mechaniclist.html', mech=mechdata)


@app.route('/areamechanic')
def areamechanic():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * from mechanic,location where mechanic.wloc=location.lid")
    mechdata = cur.fetchall()
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * from location")
    mecharea = cur.fetchall()
    cur.close()

    return render_template('areawisemechaniclist.html', mech=mechdata, mechloc=mecharea)


@app.route('/areamechanic1')
def areamechanic1():

    mechid = int(request.args.get("pid"))
    if mechid == 1:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * from mechanic,location where mechanic.wloc=location.lid")
        mechdata = cur.fetchall()
        cur.close()

    else:
        cur = mysql.connection.cursor()
        qrstr= "SELECT * from mechanic,location where mechanic.wloc=location.lid and mechanic.wloc=%s"
        locid=(mechid,)
        cur.execute(qrstr, locid)
        mechdata = cur.fetchall()
        cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * from location")
    mecharea = cur.fetchall()
    cur.close()

    return render_template('areawisemechaniclist.html', mech=mechdata, mechloc=mecharea)


@app.route('/areamechanic2')
def areamechanic2():

    mechid = int(request.args.get("pid"))
    if mechid == 1:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * from mechanic,location where mechanic.wloc=location.lid")
        mechdata = cur.fetchall()
        cur.close()

    else:
        cur = mysql.connection.cursor()
        qrstr= "SELECT * from mechanic,location where mechanic.wloc=location.lid and mechanic.wloc=%s"
        locid=(mechid,)
        cur.execute(qrstr, locid)
        mechdata = cur.fetchall()
        cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * from location")
    mecharea = cur.fetchall()
    cur.close()

    return render_template('userareawisemechaniclist.html', mech=mechdata, mechloc=mecharea)



@app.route('/addlocation')
def addlocation():  # put application's code here
    return render_template('Location.html')


@app.route('/signup')
def signup():  # put application's code here
    return render_template('signup.html')


@app.route('/signupinsert', methods = ['POST', 'GET'])
def signupinsert():  # put application's code here
     if request.method == "POST":
        name = request.form['email']
        psw = request.form['psw']

        cur = mysql.connection.cursor()
        cur.execute("insert into signup (username,password) VALUES (%s,%s)", (name, psw))
        mysql.connection.commit()
        print("inserted")
        return redirect(url_for('index'))


@app.route('/addmechanic')
def addmechanic():  # put application's code here
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from location")
    mechloc = cur.fetchall()
    cur.close()
    return render_template('mechanic.html', mechloc=mechloc)


@app.route('/editlocation')
def editlocation():  # put application's code here
    locid=int(request.args.get("id"))

    cur = mysql.connection.cursor()
    sql = "SELECT * from location where lid = %s"
    adr = (locid,)
    cur.execute(sql, adr)
    data = cur.fetchall()
    cur.close()
    return render_template('locationedit.html', placeedit=data)


@app.route('/editmech')
def editmech():  # put application's code here

    mechid = int(request.args.get("mid"))
    cur = mysql.connection.cursor()
    sql = "SELECT * from mechanic,location  where mechanic.wloc=location.lid and mechid = %s"
    adr = (mechid,)
    cur.execute(sql, adr)
    data = cur.fetchall()
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * from location")
    newdata = cur.fetchall()
    cur.close()

    return render_template('editmech.html', mechedit=data, seldata=newdata)


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == "POST":
        lid = request.form['lid']
        name = request.form['locname']
        city = request.form['city']
        loc = request.form['Loc']

        cur = mysql.connection.cursor()
        cur.execute(""" UPDATE location
         set lname=%s, lcity=%s, landmark=%s
         where lid=%s 

         """, (name, city, loc, lid))
        mysql.connection.commit()
        return redirect(url_for('location'))


@app.route('/mechupdate', methods=['POST', 'GET'])
def mechupdate():
    if request.method == "POST":
        mid = request.form['mechid']
        mname = request.form['mname']
        maddr = request.form['maddr']
        mcont = request.form['mcont']
        wname = request.form['wname']
        wloc = request.form['wloc']

        cur = mysql.connection.cursor()
        cur.execute(""" UPDATE mechanic
                 set mname=%s, maddr=%s, mcont=%s, wname=%s, wloc=%s
                 where mechid=%s 

                 """, (mname, maddr, mcont, wname, wloc,mid))
        mysql.connection.commit()
        return redirect(url_for('mechanic'))


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    id_data = int(request.args.get("id_data"))

    cur = mysql.connection.cursor()
    qstr = "DELETE FROM location where lid = %s"
    ddata=(id_data,)
    cur.execute(qstr, ddata,)
    mysql.connection.commit()
    return redirect(url_for('location'))


@app.route('/mechdelete', methods=['POST', 'GET'])
def mechdelete():
    id_data = int(request.args.get("id_mechdata"))

    cur = mysql.connection.cursor()
    qstr = "DELETE FROM mechanic where mechid = %s"
    ddata=(id_data,)
    cur.execute(qstr, ddata,)
    mysql.connection.commit()
    return redirect(url_for('mechanic'))


@app.route('/insert', methods=['POST'])
def insert():

    if request.method == "POST":
        name = request.form['name']
        city = request.form['city']
        loc = request.form['Loc']

        cur = mysql.connection.cursor()
        cur.execute("insert into location (lname,lcity,landmark) VALUES (%s,%s,%s)", (name, city, loc))
        mysql.connection.commit()
        print("inserted")
        return redirect(url_for('location'))


@app.route('/mechinsert', methods=['POST'])
def mechinsert():

    if request.method == "POST":
        mname = request.form['mname']
        maddr = request.form['maddr']
        mcont = request.form['mcont']
        wname = request.form['wname']
        loc = request.form['selloc']

        cur = mysql.connection.cursor()
        cur.execute("insert into mechanic (mname,maddr, mcont,wname,wloc) VALUES (%s,%s,%s,%s,%s)", (mname, maddr, mcont, wname, loc))
        mysql.connection.commit()
        print("inserted")
        return redirect(url_for('mechanic'))

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO : check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)
