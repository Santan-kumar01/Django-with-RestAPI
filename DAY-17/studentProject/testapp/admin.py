from django.contrib import admin
from testapp.models import Student 


class StudentAdmin(admin.ModelAdmin):

 list_display = ['rollno', 'name', 'marks', 'email']


 search_fields = ['name', 'rollno']


 list_filter = ['marks']


 ordering = ['rollno']   

admin.site.register(Student,StudentAdmin)

