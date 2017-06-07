from flask import * 

app = Flask(__name__)

#@app.route(' URL ') works over the function written imediately below it 

@app.route('/')                                     #home page - localhost:5000
def home():
	return "<h1>Welcome to home page</h1>"

@app.route('/admin/')                               #visit localhost:5000/admin
def adminpage():
	return '<i>Welcome Admin</i>'

@app.route('/guest/<nameofguest>/<contest>/')                   #visit localhost:5000/guest/<any argument to function>
def guestpage(nameofguest,contest):                           #this function accepts value to it's argument from URL
	return '<b>Welcome to %s page and %s contt</b>'%(nameofguest,contest)

"""Multiple arguments to a string format can be :
   '%s for %s' %("tit", "tat"), 
   '%(last)s, %(first)s %(last)s' %{'first': "James", 'last': "Bond"}"""

"""When a trailing slash (/) is used after an address, it becomes a canonical URL. 
Hence, using /address or /address/ returns the same output. 
However, if code does not have trailing slash (/) in address, URL results in 404 Not Found page."""

@app.route('/users/<argument>/<contestarg>')                     
def users(argument,contestarg):                             
    if argument=="admin":                            #checks if argument is admin, sent to adminpage function
    	return redirect(url_for('adminpage'))
    else:                                           #else, sent to guestpage function with argument passed
    	return redirect(url_for('guestpage',nameofguest=argument,contest=contestarg))
	
if __name__ == '__main__':
	app.debug = True                                  # to make changes dynamically in code and see results
	app.run(host=None,port=None)                      # takes default 127.0.0.1:5000
	
""" To make app run on different port specify app.run(host="0.0.0.0",port=<anyvalue>)"""   
# host depends on server and port depends on user port = <any value>

