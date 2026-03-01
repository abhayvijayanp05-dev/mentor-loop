from django.conf.urls import url
from assignment_upload import views

urlpatterns = [
    url('add/', views.post_assignment),
    url('view/', views.viewassignmentteacher),
    url('grade/(?P<idd>\w+)',views.grade),
    url('vgrade/', views.viewgrade ),
    url('vgradeparent/', views.viewgradeparent),
    url('vgradeteacher/', views.viewteacher),
    url('viewstudent/', views.viewassignmentstudent),
    url('edit_assignment/(?P<idd>\w+)', views.post_assignment_edit)

]