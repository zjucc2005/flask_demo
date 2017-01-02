# URL routes and views for the app
import datetime
from flask import render_template, redirect, flash, request, url_for
from flask_login import login_user, logout_user

from app import app, login_manager
from forms import LoginForm

@app.route('/')
def homepage():
	name = request.args.get('name')
	number = request.args.get('number')
	format_current_time = datetime.datetime.now().strftime('%Y:%m:%d %H:%M:%S')
	app.logger.info('%s -- Homepage has been accessed by cc.' % format_current_time)
	app.logger.warning('{current_time} -- An Exception has been thrown out.'.format(current_time = format_current_time))
	return render_template('homepage.html', name=name, number=number)

@app.route('/login/', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		form = LoginForm(request.form)
		if form.validate():
			login_user(form.user, remember = form.remember_me.data)
			flash('Successfully logged in as %s.' % form.user.email, 'success')
			return redirect(request.args.get('next') or url_for('homepage'))
	else:
		form = LoginForm()
	return render_template('login.html', form = form)

@app.route('/logout/')
def logout():
	logout_user()
	flash('You have been logged out.', 'success')
	return redirect(request.args.get('next') or url_for('homepage'))
