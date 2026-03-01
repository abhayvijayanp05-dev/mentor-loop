from django.conf.urls import url
from doubt import views

urlpatterns = [
    url('add/', views.post_doubts),
    url('reply/(?P<idd>\w+)', views.reply_for_doubts),
    url('view/', views.view_doubt),
    url('doubt/', views.view_reply),
    url('teacher/',views.view_reply_teacher)

]