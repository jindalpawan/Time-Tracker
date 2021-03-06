from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	name = models.CharField(max_length = 200, unique = True)

	def __str__(self):
		return self.name

class Timing(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	project = models.ForeignKey(Project, on_delete = models.CASCADE)
	task = models.CharField(max_length = 200) # task name
	start = models.DateTimeField(auto_now_add = True) # start time will be the time of creating an object
	end = models.DateTimeField(default = None, null = True)

	def __str__(self):
		return self.task
