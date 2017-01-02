import unittest
from flask import request
from main import app
import json

class AppTest(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()

	def tearDown(self):
		pass

	def test_homepage_works(self):
		response = self.app.get('/')
		self.assertEqual(response.status_code, 200)

class APITest(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()
		self.comment_data = {
		'name':       'unittest',
		'email':      'unit@test.com',
		'url':        'http://localhost',
		'ip_address': '127.0.0.1',
		'body':       'This is a unittest comment.',
		'entry_id':   1
		}

	def test_getting_comment(self):
		comment = self.app.get('/api/comment/1')
		response = self.app.get('/api/comment')
		self.assertEqual(response.status_code, 200)
		self.assertTrue(json.loads(comment.data) in json.loads(response.data)['objects'])


if __name__ == '__main__':
	unittest.main()