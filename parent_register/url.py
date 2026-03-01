from django.conf.urls import url
from parent_register import views

urlpatterns = [
    url('add/', views.registerparent),
    url('view/', views.viewparent),
    url('manage/', views.parent_management),
    url('accept/(?P<idd>\w+)',views.accept),
    url('reject/(?P<idd>\w+)',views.reject),
    url('parent_profile/', views.parent_profile)
]

