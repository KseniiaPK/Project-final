from django.db import models

# Create your models here.
class Student(models.Model):
    Username = models.CharField(max_length=30, unique=True)
    Password = models.CharField(max_length=64)
    Name = models.CharField(max_length=60)
    Surname = models.CharField(max_length=60)
    Photo = models.ImageField(upload_to="images/", blank=True, null=True)

class Teacher(models.Model):
    Username = models.CharField(max_length=30, unique=True)
    Password = models.CharField(max_length=64)
    Name = models.CharField(max_length=60)
    Surname = models.CharField(max_length=60)
    Photo = models.ImageField(upload_to="images/", blank=True, null=True)
    Bio = models.CharField(max_length=200)


class Subject(models.Model):
    Name = models.CharField(max_length=60, unique=True)


class Course(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    Subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    Teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    Info = models.CharField(max_length=200)
    Price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


class Enrollment(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.PROTECT)
    Course = models.ForeignKey(Course, on_delete=models.PROTECT)
