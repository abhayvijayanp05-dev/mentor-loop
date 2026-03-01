from django.conf.urls import url
from complaint import views

urlpatterns = [
    url('add/', views.postcompaints),
    url('reply/(?P<idd>\w+)', views.replycomplaints),
    url('view/', views.viewcomplaints),
    url('vr/', views.viewcomplaintsreply),
   url('vradmin/', views.viewcomplaintsreplyadmin)

    ]