from django.shortcuts import render
from testapp.forms import StudentForm

# Create your views here.
def student_input_view(request):
    forms = StudentForm()

    return render(request,'testapp/student.html',{'form':forms})
