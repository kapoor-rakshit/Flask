from flask import *

app=Flask(__name__)

@app.route('/')
def home():
	return render_template("filedownload.html")

"""send_file is the function that handles sending files to the user. 
It does no sanity check on the input, so it would also happily send protected/../../../etc/passwd or whatever.
Being unaware of that type of attack you might produce unsecure code."""

@app.route('/downloadsendfile/')
def sendfile():
	try:
		return send_file("C:\\Users\\R6000670\\Desktop\\R6000670 docs\\scan4.pdf",attachment_filename="sem.pdf")
	except Exception as e:
		return str(e)

"""send_from_directory checks wether the requested file is really from the specified directory. 
That way the above attack would not work."""

@app.route('/downloadsendfromdirectory')
def sendfromdirectory():
	try:
		return send_from_directory("C:\\Users\\R6000670\\Desktop\\R6000670 docs\\","scan4.pdf")
	except Exception as e:
		return str(e)


""" use send_file whenenver the input filepath is trusted. 
That means either do your own checks or if the input is provided by you (e.g. my_file_paths = {"a": "path/to/a", ... }; send_file(my_file_paths[user_input]) would be okay) you should be fine. 
For the common case send_from_directory is a helper function that does the appropriate security checks."""

if __name__=='__main__':
	app.debug=True
	app.run(port=8888)