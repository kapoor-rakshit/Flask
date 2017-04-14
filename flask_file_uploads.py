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
