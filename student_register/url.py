from django.conf.urls import url
from student_register import views

urlpatterns = [
    url('add/', views.Registerstudent),
    url('view/', views.viewstudent),
    url('manage/', views.student_management),
    url('edit/(?P<idd>\w+)',views.edit),
    url('view_profile/', views.student_profile)

]


