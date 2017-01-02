from flask_mail import Mail, Message
from main import app, celery

mail = Mail(app)

"""
@celery.task
def senf_password_verification(email, verification_code):
	msg = Messsage(
		'Your password reset verification code is: {code}'.format(code = verification_code),
		sender = 'from@example.com',
		recipients = [email]
		)
	mail.send(msg)
"""