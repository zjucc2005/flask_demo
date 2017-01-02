# Configuration variables for our Flask app
import os
class Configuration(object):
	APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
	DEBUG = True
	SECRET_KEY = 'quaieapp' 
	# SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/blog.db' % APPLICATION_DIR
	SQLALCHEMY_DATABASE_URI = 'mysql://flask_test:123456@localhost/flask_db'
	# if want to connect to PostgreSQL, URI may look like as below
	# postgresql://postgres:password@localhost:5432/blog_db
	# refer to http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	# SQLALCHEMY_TRACK_MODIFICATIONS:
	# If set to True, Flask-SQLAlchemy will track modifications of objects and emit 
	# signals. The default is None, which enables tracking but issues a warning that
	# it will be disabled by default in the future. This requires extra memory and 
	# should be disabled if not needed.
	STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')
	IMAGES_DIR = os.path.join(STATIC_DIR, 'images')

	# CSRF_COOKIE_NAME = '_csrf_token'

	# MAIL_SERVER   = 'example.com'
	# MAIL_PORT     = 25
	# MAIL_USERNAME = 'email_username'
	# MAIL_PASSWORD = 'email_password'