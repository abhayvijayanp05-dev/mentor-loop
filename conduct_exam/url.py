from django.conf.urls import url
from conduct_exam import views

urlpatterns = [
    url('add/', views.conductexam),
    url('exam/(?P<idd>\w+)', views.examquestion),
    url('view/', views.view_conduct_exam),
    url('ve/', views.view_conduct_exam_student),
    url('veteacher/', views.view_conduct_exam_teacher),
    url('viteacher/', views.view_exam_teacher)


]