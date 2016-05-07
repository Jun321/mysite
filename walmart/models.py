from django.db import models
from datetime import datetime

# Create your models here.

class User(models.Model):
	user_name = models.CharField(max_length=20)
	user_password = models.CharField(max_length=200)
	register_time = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return self.user_name


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=20)
	text = models.CharField(max_length=500)
	pub_time = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return self.title