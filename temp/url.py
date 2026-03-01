from django.conf.urls import url
from temp import views

urlpatterns = [
    url('admin/', views.admin),
    url('home/',views.home),
    url('parent/', views.parent),
    url('student/',views.student),
    url('teacher/',views.teacher)
]