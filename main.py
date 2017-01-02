# Entry-point for executing our application
# from flask import request, session

from app import app, db # import Flask app
import admin # should loaded after app
import api
import models
import views

#from celery import Celery
#celery = Celery(app.name, broker = app.config['CELERY_BROKER_URL'])

from entries.blueprint import entries
app.register_blueprint(entries, url_prefix = '/entries')


if __name__ == '__main__':
	app.run()