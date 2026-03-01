from django.conf.urls import url
from feedback import views

urlpatterns = [
    url('add/', views.parentfeedback),
    url('view/', views.view_feedback),
    url('viewteacher/', views.view_feedback_teacher)

]