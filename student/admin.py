from django.contrib import admin

# Register your models here.
from .models import *
from django.db.models import Sum

admin.site.register(StudentId)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)

class SubjectMarkAdmin(admin.ModelAdmin):
    list_display = ['student','subject','marks']


admin.site.register(SubjectMark,SubjectMarkAdmin)

class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student','student_rank','total_marks','date_of_report_card_genration']
    # ordering = ['studnet_rank']
    def total_marks(self,obj):
        subject_mark = SubjectMark.objects.filter(student = obj.student)
        marks = (subject_mark.aggregate(marks=Sum('marks')))
        return marks['marks']
admin.site.register(ReportCard,ReportCardAdmin)

