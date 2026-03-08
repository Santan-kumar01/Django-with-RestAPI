from django.contrib import admin

from testapp.models import FilterModel

class FilterModelAdmin(admin.ModelAdmin):
    list_display = ['name','subject','dept','date']


admin.site.register(FilterModel,FilterModelAdmin)    
# Register your models here.
