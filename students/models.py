from django.db import models

class Faculty(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class Course(models.Model):
	faculty = models.ForeignKey(Faculty,null=True,on_delete=models.CASCADE)
	name = models.CharField(max_length = 255)
	def __str__(self):
		return self.name

class Stage(models.Model):
	stage = models.CharField(max_length = 255)
	def __str__(self):
		return self.stage

class Group(models.Model):
	faculty = models.ForeignKey(Faculty,null=True,on_delete=models.CASCADE)
	course = models.ForeignKey(Course,null=True,on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=255)
	stage = models.ForeignKey(Stage,on_delete=models.CASCADE)
	group = models.ForeignKey(Group,on_delete=models.CASCADE)
	faculty = models.ForeignKey(Faculty,null=True,on_delete=models.CASCADE)
	course = models.ForeignKey(Course,null=True,on_delete=models.CASCADE)
