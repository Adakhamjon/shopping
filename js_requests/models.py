from django.db import models

class Comment(models.Model):
	text = models.CharField(max_length=255)
	user = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)
