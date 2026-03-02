from django.shortcuts import render
from testapp.models import Course
# Create your views here.
def course_view(request):
    courses = Course.objects.all()

    return render(request,'testapp/index.html',{'courses':courses})
