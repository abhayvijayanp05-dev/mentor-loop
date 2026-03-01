from django.conf.urls import url
from document import views

urlpatterns = [
    url('add/', views.upload_document),
    url('view/', views.view_document),
    url('viewteacher/', views.view_document_teacher),
    url('edit/(?P<idd>\w+)', views.upload_document_edit),

]