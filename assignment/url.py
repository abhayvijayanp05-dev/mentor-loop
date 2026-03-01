from django.conf.urls import url
from assignment import views
urlpatterns=[
    url('add/',views.add_assignment),
    url('view/',views.viewassignment),
    url('viewteacher/', views.viewassignment_teacher)

]