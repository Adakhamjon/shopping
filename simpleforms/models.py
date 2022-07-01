from django.db import models


class Genre(models.Model):
	name = models.CharField(max_length = 255)
	def __str__(self):
		return self.name

class Books(models.Model):
	title = models.CharField(max_length=255)
	author = models.CharField(max_length = 255)
	genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
	year = models.CharField(max_length = 255)
	image = models.ImageField(upload_to="images/")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.title

class Filial(models.Model):
	title = models.CharField(max_length=255)
	established_at = models.DateTimeField()

	def __str__(self):
		return self.title

class Director(models.Model):
	filial = models.OneToOneField(Filial,on_delete=models.CASCADE)
	fullname = models.CharField(max_length=255)
	experience = models.PositiveIntegerField(null=True)
	def __str__(self):
		return self.fullname

class Actor(models.Model):
	fullname = models.CharField(max_length=255)
	age = models.CharField(max_length=255)
	def __str__(self):
		return self.fullname

class Movie(models.Model):
	title = models.CharField(max_length=255)
	release_date = models.DateTimeField()
	actors = models.ManyToManyField(Actor)
	def __str__(self):
		return self.title

