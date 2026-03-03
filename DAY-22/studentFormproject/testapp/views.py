from django.shortcuts import render
from testapp.forms import StudentForm 


def register(request):

    form = StudentForm(request.POST or None)

    if request.method == "POST" and form.is_valid():

        # Create your views here.

        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        desc = form.cleaned_data['description']

        print(f'Name: {name}')
        print(f'Email: {email}')
        print(f'Description: {desc}')

        data_dict = {
            'name': name,
            'email': email,
            'desc': desc
        }

        return render(request, 'testapp/data.html', {'data_dict': data_dict})

    return render(request, 'testapp/student.html', {'form': form})