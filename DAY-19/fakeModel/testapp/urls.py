
from django.urls import path
from testapp import views 

urlpatterns = [
    path('studnet/',views.student_view),
    path('student/api/',views.student_json_view),
]
