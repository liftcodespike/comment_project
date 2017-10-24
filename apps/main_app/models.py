from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User

# Create your models here.


class CommentManager(models.Manager):
	def validate(self, postData):
		results = {'errors':[]}
		if len(postData['content']) < 3:
			results['errors'].append('Comment must be at least 3 chars.')
		if len(postData['poster_id']) == 0:
			results['errors'].append('Something went wrong. Try again friend.')
		if len(postData['user_id']) == 0:
			results['errors'].append('Something went wrong. Try again friend.')
		return results



class Comment(models.Model):
	content = models.CharField(max_length = 255)
	poster = models.ForeignKey(User, related_name='posts')
	user = models.ForeignKey(User, related_name='comments')
	objects = CommentManager()


