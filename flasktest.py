from flask import * 

app = Flask(__name__)

#@app.route(' URL ') works over the function written imediately below it 

@app.route('/')                                     #home page - localhost:5000
def home():
	return "<h1>Welcome to home page</h1>"

@app.route('/admin/')                               #visit localhost:5000/admin
def adminpage():
	return '<i>Welcome to Admin page</i>'

@app.route('/guest/<nameofguest>/')                   #visit localhost:5000/guest/<any argument to function>
def guestpage(nameofguest):                           #this function accepts value to it's argument from URL
	return '<b>Welcome to %s page </b>'%nameofguest

"""When a trailing slash (/) is used after an address, it becomes a canonical URL. 
Hence, using /address or /address/ returns the same output. 
However, if code does not have trailing slash (/) in address, URL results in 404 Not Found page."""

@app.route('/users/<argument>/')                     
def users(argument):                             
    if argument=="admin":                            #checks if argument is admin, sent to adminpage function
    	return redirect(url_for('adminpage'))
    else:                                           #else, sent to guestpage function with argument passed
    	return redirect(url_for('guestpage',nameofguest=argument))
	
if __name__ == '__main__':
	app.debug = True                                  #to make changes dynamically in code and see results
	app.run()
