from flask import *

app=Flask(__name__)
app.secret_key = 'random string'

#A Flask module contains flash() method. 
#It passes a message to the next request, which generally is a template.

#flash(message, category)
#message parameter is the actual message to be flashed.
#category parameter is optional. It can be either error, info or warning.

@app.route('/')
def home():
	return render_template('login.html')

@app.route('/check/', methods=["post"])
def check():
	user=request.form['user']
	password=request.form['pass']
	if user=="guest" and password=="guestpass":
		flash("Login Successful")
		flash("Login Another")
		return redirect(url_for("home"))
	else:
		flash("Login Attempt Failed")
		flash("Try Again")
		return redirect(url_for("home"))

if __name__=='__main__':
	app.debug=True
	app.run()