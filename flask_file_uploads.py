# A <form> tag is marked with enctype=multipart/form-data and an <input type=file> is placed in that form.
# The application accesses the file from the files dictionary on the request object.
# use the save() method of the file to save the file permanently somewhere on the filesystem.

# secure_filename() function actually do?  
# All submitted form data can be forged, and filenames can be dangerous. 
# So always use that function to secure a filename before storing it directly on the filesystem.

# just imagine someone would send the following information as filename to your application:
#                         filename = "../../../../home/username/.bashrc"

# Assuming the number of ../ is correct.
# You would join this with the UPLOAD_FOLDER the user might have the ability to modify a file on the server’s filesystem. 

from flask import *
from werkzeug import secure_filename

app=Flask(__name__)

@app.route('/')
def home():
	return render_template('fileupload.html')

@app.route('/results',methods=['post'])
def results():
	file=request.files['file']
	file.save(secure_filename(file.filename))
	contenttype=file.content_type
	buffer=[]
	buffer.append(file.stream.read())
	return render_template('fileresults.html',content=buffer,contenttype=contenttype)

if __name__ == '__main__':
	app.debug=True
	app.run()

	
#To upload file to a folder (whether present or not in PC)

import os
from flask import *
from werkzeug import secure_filename
from flask import send_from_directory

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER="C:/Users/R6000670/Documents/Neo4j/pracneo/data/csv/"

app=Flask(__name__)
app.secret_key = 'random string'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_files(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/results/',methods=['post'])
def results():
	file=request.files['file']
	if file.filename=='':
		flash("No file was selected !!")
		flash("Choose your file again")
		return redirect(url_for("home"))
	elif not allowed_files(file.filename):
		flash("Invalid file !!")
		flash("Choose your file again")
		return redirect(url_for("home"))
	else:
		securedfile=secure_filename(file.filename)

		if not os.path.exists(UPLOAD_FOLDER):
			os.makedirs(UPLOAD_FOLDER)

		file.save(os.path.join(app.config['UPLOAD_FOLDER'], securedfile))

		ctype=file.content_type

		#return render_template('resultspage.html',contenttype=ctype)
		return redirect(url_for("uploaded",securedfile=securedfile))

@app.route('/uploads/<securedfile>')
def uploaded(securedfile):
	return send_from_directory(app.config['UPLOAD_FOLDER'],securedfile)

if __name__=='__main__':
    app.debug=True
    app.run()
	
	
