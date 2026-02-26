from django.shortcuts import render

def student_data(request):
    student_profile = {
        # Key:value

        'name':'Nobita',
        'age':25,
        'course':'Python full Stack Developer'
    
    }
    
    return render(request,'testapp/index.html',context=student_profile)