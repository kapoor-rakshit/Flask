from flask import *

app=Flask(__name__)

@app.route('/')
def home():
	l=[-3,-888,9,6,4,-55]
	k=["kapoor","amritsar","NITJ","intern @ Wipro"]
	kk="Hello filters awesome work by jinja developers"
	return render_template('filters.html',l=l,k=k,kk=kk)

if __name__=='__main__':
	app.debug=True
	app.run(host="0.0.0.0",port=8888)