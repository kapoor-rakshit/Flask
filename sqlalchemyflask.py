# Reference : https://www.tutorialspoint.com/flask/flask_sqlalchemy.htm
# Install Flask-SQLAlchemy extension :     pip install flask-sqlalchemy

from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "random string"
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///studdb.sqlite3"

db = SQLAlchemy(app)

class stud(db.Model):                          # flask-sqlalchemy creates table automatically with name of baseclass
	roll = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String(20), nullable = False)
	                                           # column names are variable to which assigned i.e. roll, name

	def __init__(self, roll, name):
		self.roll = roll
		self.name = name

@app.route("/")
def home():
	return render_template("sqlalchemyflaskhome.html",res = stud.query.all())
	                                            # modelclass.query.all()   -    selects all rows from table
	                                            # modelclass.query.filter_by(roll=4084).all()  -  selects with roll = 4084

@app.route("/rec/", methods=["post"])
def res():
	try:
		roll = request.form["roll"]
		name = request.form["name"]

		studdata = stud(roll,name)              # model object 'studdata' for model class 'stud'

		db.session.add(studdata)                # insertion
		db.session.commit()

		flash("Recorded Successfully")
		return redirect(url_for("home"))
	except Exception as e:
		flash(str(e))
		return redirect(url_for("home"))

@app.route("/del/",methods=["post"])
def deletefunc():
	stud.query.filter_by(roll=9025).delete()   # deletion
	db.session.commit()
	flash("Deleted")
	return redirect(url_for("home"))

@app.route("/upd/",methods=["post"])
def updatefunc():
	studinstance = stud.query.get(4084)        # get record by primary_key
	studinstance.name = "tak"                  # upadte column
	db.session.commit()
	flash("Updated")
	return redirect(url_for("home"))

if __name__ == '__main__':
	db.create_all()                            # To create/use database mentioned in URI, run the create_all() method.
	app.debug = True
	app.run()