from django.db import models
from datetime import datetime

# Create your models here.

class Comment(models.Model):
	user = models.CharField(max_length=20)
	title = models.CharField(max_length=20)
	text = models.CharField(max_length=500)
	pub_time = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return self.title