from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class StudentId(models.Model):
    id_number = models.CharField(max_length=100)

    def __str__(self):
        return self.id_number

class Student(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    student_id = models.OneToOneField(StudentId, on_delete=models.CASCADE, related_name='student')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=18)
    address = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "student"
