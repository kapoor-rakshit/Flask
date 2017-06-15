from flask import *

app=Flask(__name__)

@app.route('/')
def home():
	return render_template('login.html')

@app.route('/check/', methods=["post"])
def check():
	if request.form['user']=="guest" and request.form['pass']=="guestpass":
		return "Login Successful"
	else:
		return redirect(url_for('home'))                              #redirect to login page 
	
	"""-------------ANOTHER WAY ROUND using try except-----------------------"""
	
@app.route('/check/',methods=["post"])
def check():
	try:
		#your code here
		return render_template("success.html")
	except Exception as e:
		return render_template("error.html", error=str(e))
		

#Flask.redirect(location, statuscode, response)
#In the above function

#location parameter is the URL where response should be redirected.
#statuscode sent to browsers header, defaults to 302.
#response parameter is used to instantiate response.

#The following status codes are standardized :
#HTTP_300_MULTIPLE_CHOICES
#HTTP_301_MOVED_PERMANENTLY
#HTTP_302_FOUND
#HTTP_303_SEE_OTHER
#HTTP_304_NOT_MODIFIED
#HTTP_305_USE_PROXY
#HTTP_306_RESERVED
#HTTP_307_TEMPORARY_REDIRECT

		'''abort(401)'''                                                   #abort on call  

#Flask.abort(code)
#The Code parameter takes one of following values

#400  for Bad Request
#401  for Unauthenticated
#403  for Forbidden
#404  for Not Found
#406  for Not Acceptable
#415  for Unsupported Media Type
#429  Too Many Requests"""

@app.errorhandler(404)
def page_error(e):
	return render_template("error.html")

if __name__=='__main__':
	app.debug=True
	app.run()

