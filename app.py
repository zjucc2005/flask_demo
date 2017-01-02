# The Flask app
from flask import Flask, g
from flask_login      import LoginManager, current_user
from flask_bcrypt     import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate    import Migrate, MigrateCommand
from flask_script     import Manager
# a third-party Flask extension that makes it simple to build RESTful APIs for SQLAlchemy
from flask_restless   import APIManager
# build CSRF protection 
from flask_seasurf import SeaSurf

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration) # use values from our Configuration object
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

api = APIManager(app, flask_sqlalchemy_db = db) # => api.py

@app.before_request
def _before_request():
	g.user = current_user

bcrypt = Bcrypt(app)
# a set of variable can be added into configuration file
# CSRF_COOKIE_NAME, CSRF_COOKIE_TIMEOUT, CSRF_COOKIE_HTTPONLY, CSRF_COOKIE_SECURE, CSRF_DISABLE
# csrf   = SeaSurf(app)

# writing logs to a file named blog.log
from logging.handlers import RotatingFileHandler
file_handler = RotatingFileHandler('blog.log')
app.logger.addHandler(file_handler)
