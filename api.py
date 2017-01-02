from flask_restless import ProcessingException

from app import api
from models import Comment
from entries.forms import CommentForm

# Using the POST preprocessor to validate data in the API
def post_preprocessor(data, **kwargs):
	form = CommentForm(data = data)
	if form.validate():
		return form.data
	else:
		raise ProcessingException(description = 'Invalid form submission.', code = 400)
"""
api configuration
include_column and include methods decide columns of response data, there is a sample below
ordered by initial alphabet, JSON
{
  "body": "Test comment!", 
  "created_timestamp": "2016-12-28T17:21:33", 
  "gravatar": "http://www.gravatar.com/avatar.php?size=75&gravatar_id=bab8184b7b2595b6388afbfdf61101bc", 
  "id": 1, 
  "name": "caichang", 
  "url": null
}
"""
api.create_api(
	Comment, 
	include_columns = ['id', 'name', 'url', 'body', 'created_timestamp'],
	include_methods = ['gravatar'],
	methods = ['GET', 'POST'], # 'DELETE'
	preprocessors = { 'POST': [post_preprocessor] }
	)
