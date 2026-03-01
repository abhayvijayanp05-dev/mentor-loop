from django.conf.urls import url
from teacher_register import views

urlpatterns = [
    url('add/', views.teacherRegister),
    url('view/', views.viewteacher),
    url('manage/', views.teacher_management),
    url('accept/(?P<idd>\w+)',views.accept),
    url('reject/(?P<idd>\w+)',views.reject),
    url('view_profile/', views.teacher_profile)
]