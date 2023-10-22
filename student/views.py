from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q,Sum

# Create your views here.
def get_students(request):
        
    queryset = Student.objects.all()

    

    paginator = Paginator(queryset, 10)  
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    return render (request,'student.html',{'results':page_obj})

def search_view(request):
    search = request.GET.get('search')
    results = Student.objects.filter(
        Q(student_email__icontains=search) |
        Q(student_name__icontains=search) | 
        Q(department__department__icontains=search) |
        Q(student_age__icontains=search)

        )
    context = {
        'search': search,
        'results': results,
    }
    return render(request,'student.html', context)


from .seed import generate_report_card
def see_mark (request,studentid):
    # generate_report_card()
    queryset = SubjectMark.objects.filter(student__studentid__studentid = studentid)
    total_marks = queryset.aggregate(total_marks = Sum ('marks'))
    
    
    return render(request,'see_mark.html',{'queryset':queryset,'total_marks' : total_marks})
