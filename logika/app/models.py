from django.db import models
class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    def __str__(self):
        return self.name

class Teacher(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.firstname}  {self.lastname}"

class ClassRoom(models.Model):
    name = models.CharField(max_length=100, unique=True)
    year = models.IntegerField()
    def __str__(self):
        return self.name
class Student(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.firstname}  {self.lastname}"

class Schedule(models.Model):
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.day}  {self.time}"
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mark = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return f"{self.student}  {self.mark}"

