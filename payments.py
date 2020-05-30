from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(host="localhost", database="magicspaces", user="postgres", password="pgpass")
cur = conn.cursor()

@app.route('/')
def index():
        return render_template("parent.html")

@app.route("/parent", methods=["GET", "POST"])
def parent():  
    if request.method == "POST":
        fname = request.form["username"]
        cur.execute("SELECT clientid FROM registration WHERE username= %s",(fname,))
        clients = cur.fetchall()
        for item in clients:
            client = item[0]
       
        cur.execute("SELECT * FROM payments WHERE clientid = %s", (client,))
        qresult = cur.fetchall()
        return render_template("payments.html", values = qresult)


@app.route("/payments", methods=["GET", "POST"])
def payments():
    if request.method == "POST":

        #fname = request.form["username"]
        fname='anil'
        cur.execute("SELECT clientid FROM registration WHERE username= %s",(fname,))
        clients = cur.fetchall()
        for item in clients:
            client = item[0]

        newdesc = request.form["paydescription"]
        newdate = request.form["paydate"]
        newamt = request.form["payamount"]
        newmethod = request.form["paymethod"]

        cur.execute('Insert into payments ("payDescription", "payDate", "payamount", "paymethod", "clientid") values (%s, %s, %s, %s, %s)',(newdesc, newdate, newamt, newmethod, client,))
        conn.commit()
        
        cur.execute("SELECT * FROM payments WHERE clientid = %s", (client,))
        qresult = cur.fetchall()
        return render_template("payments.html", values = qresult)
    else:
        cur.execute("SELECT * FROM payments")
        qresult = cur.fetchall()
        return render_template("payments.html", values = qresult)
    

if __name__ == "__main__":
    app.run(debug = True)
