from django.shortcuts import render
from django.http import HttpResponse

# Home View
def home_view(request):
    return render(request, 'testapp/home.html')


# Age View (GET parameters + Cookies)
def age_view(request):
    name = request.GET.get('name')
    age = request.GET.get('age')

    response = render(request, 'testapp/age.html', {'name': name, 'age': age})
    
    # Cookies set
    response.set_cookie('name', name)
    response.set_cookie('age', age)

    return response


# Course View (GET parameters + Cookies)
def course_view(request):
    course = request.GET.get('course')

    response = render(request, 'testapp/course.html', {'course': course})
    
    # Cookie set
    response.set_cookie('course', course)

    return response


# Result View (Read Cookies)
def result_view(request):
    name = request.COOKIES.get('name')
    age = request.COOKIES.get('age')
    course = request.COOKIES.get('course')

    return render(request, 'testapp/results.html', {
        'name': name,
        'age': age,
        'course': course
    })