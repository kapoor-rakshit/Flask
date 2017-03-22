from flask import *

app=Flask(__name__)

@app.route('/')
def home():
	return "WELCOME"

@app.route('/login/')
def login():
	return render_template('login.html')

@app.route('/info',methods=['POST','GET'])
def info():
	if request.method == 'POST':
		firstname = request.form['firstname']
		lastname = request.form['lastname']
		gender = request.form['gender']
		interests = request.form.getlist('interests')
		bday = request.form['bday']
		email = request.form['email']
		year = request.form['year']
		return render_template('results.html',first=firstname,last=lastname,gen=gender,inst=interests,dt=bday,mail=email,yr=year)
	else:
		firstname = request.args.get('firstname')
		lastname = request.args.get('lastname')
		gender=request.args.get('gender')
		interests=request.args.get('interests')
		bday=request.args.get('bday')
		email=request.args.get('email')
		year=request.args.get('year')
		return render_template('results.html',first=firstname,last=lastname,gen=gender,inst=interests,dt=bday,mail=email,yr=year)

if __name__=='__main__':
	app.debug=True
	app.run()
