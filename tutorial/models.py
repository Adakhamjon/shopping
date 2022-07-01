from django.db import models
class Subject(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class Teacher(models.Model):
	subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=255)
	subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
	teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
	
