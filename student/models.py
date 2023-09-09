from django.db import models

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department']
    
class StudentId (models.Model):
    Student_Id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Student_Id
    
class Student(models.Model):
    department = models.CharField(Department, related_name='depart',on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentId, related_name='studentid',on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        odering = ['student_name']
        verbose_name = "student"

        

