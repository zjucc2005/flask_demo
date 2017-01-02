from flask import g
import wtforms
from wtforms.validators import *

from app import app
from models import User

class SeaSurfForm(wtforms.Form):
	pass
	"""
	@staticmethod
	@app.before_request
	def add_csrf():
		csrf_name = app.config.get('CSRF_COOKIE_NAME', '_csrf_token')
		setattr(SeaSurfForm, csrf_name, wtforms.HiddenField(default = getattr(g, csrf_name)))
	"""

class LoginForm(SeaSurfForm):
	email       = wtforms.StringField('Email', validators = [DataRequired(), Email()])
	password    = wtforms.PasswordField('Password', validators = [DataRequired()])
	remember_me = wtforms.BooleanField('Remember me?', default = True)

	def validate(self):
		# invoke subclass's validate method, execute validators
		if not super(LoginForm, self).validate():
			return false
		self.user = User.authenticate(self.email.data, self.password.data)
		# append additional messages to error list
		if not self.user:
			self.email.errors.append('Invalid email or password.')
			return False
		return True