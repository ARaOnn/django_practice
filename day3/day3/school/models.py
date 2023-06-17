from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	year = models.IntegerField()
class Book(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
class Course(models.Model):
	title = models.CharField(max_length=100)
	students = models.ManyToManyField(Student)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)