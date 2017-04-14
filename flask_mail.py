# Message
# ( subject='', recipients=None, body=None, html=None, sender=None, cc=None, bcc=None, attachments=None, 
# reply_to=None, date=None, charset=None, extra_headers=None, mail_options=None, rcpt_options=None )
# Encapsulates an email message.

# attach
# (filename=None, content_type=None, data=None, disposition=None, headers=None)
# Adds an attachment to the message.
# Parameters:	
# filename – filename of attachment
# content_type – file mimetype
# data – the raw file data
# disposition – content-disposition (if any)


from flask import *
from flask_mail import Mail, Message

app=Flask(__name__)

mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'rakshitk.ec.14@nitj.ac.in'
app.config['MAIL_PASSWORD'] = '****Password****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def home():
	msg = Message('FlaskMessage', sender = 'rakshitk.ec.14@nitj.ac.in', recipients = ['adhish.kapoor@yahoo.co.in'])
	msg.body = "Hello Flask message sent from Flask-Mail"
	with app.open_resource("Notes.txt") as fp:
		msg.attach("Notes.txt","txt", fp.read())
	mail.send(msg)
	return "Sent"


if __name__ == '__main__':
	app.debug = True
	app.run()
