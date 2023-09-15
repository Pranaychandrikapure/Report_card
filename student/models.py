from django.db import models


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department

    class Meta:
        ordering = ['department']

class StudentId(models.Model):
    studentid = models.CharField(max_length=100)

    def __str__(self):
        return self.studentid
    
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name
    


class Student(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='depart')
    studentid = models.OneToOneField(StudentId, on_delete=models.CASCADE, related_name='student')
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self):
        return self.student_name

    class Meta:
        ordering = ['student_name']
        verbose_name = "student"
    
class SubjectMark(models.Model):
    student = models.ForeignKey(Student,related_name="studentmark",on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.student.student_name} {self.subject.subject_name}'

    class Meta :
        unique_together = ['student','subject']