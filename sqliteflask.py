# Reference : https://www.tutorialspoint.com/flask/flask_sqlite.htm

from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'random string'

@app.route("/")
def home():
	return render_template("sqliteflaskhome.html")

@app.route("/result/", methods=["post"])
def results():
	try:
		conn = sql.connect("studrecord.db")
		cursor = conn.execute("select * from stud;")
		allrows = cursor.fetchall()                                      # a list with required values
		return render_template("sqliteflaskresult.html",rows = allrows)
	except Exception as e:
		flash(str(e))
		return redirect(url_for("home"))

@app.route("/rec/", methods=['post'])
def record():
	if request.form['name']=='' or request.form['roll']=='':
		flash("Please fill in all fields")
		return redirect(url_for("home"))
	else:
		try:
			name = request.form['name']
			roll = request.form['roll']

			with sql.connect("studrecord.db") as conn:
				chk = conn.execute("select name from sqlite_master where name = 'stud' and type = 'table';")
				val = chk.fetchall()                                 # check if table exists or not
				if len(val) == 0:                                    # if not create 
					conn.execute("create table stud (ROLL_NO INTEGER PRIMARY KEY NOT NULL, NAME TEXT NOT NULL);")

				conn.execute("insert into stud values(?,?);",(roll,name))
				conn.commit()
			flash("Recorded successfully.")
		except Exception as e:
			conn.rollback()
			flash(str(e))
		finally:
			conn.close()
			return redirect(url_for("home"))

if __name__ == "__main__":
	app.debug = True
	app.run()