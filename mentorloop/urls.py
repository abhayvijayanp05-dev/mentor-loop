"""mentorloop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from temp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url('assignment/',include('assignment.url')),
    url('assignment_upload/',include('assignment_upload.url')),
    url('complaint/', include('complaint.url')),
    url('conduct_exam/', include('conduct_exam.url')),
    url('document/', include('document.url')),
    url('doubt/', include('doubt.url')),
    url('feedback/', include('feedback.url')),
    url('login/', include('login.url')),
    url('parent_register/', include('parent_register.url')),
    url('student_register/', include('student_register.url')),
    url('teacher_register/', include('teacher_register.url')),
    # url('uploadanswer_exam/', include('uploadanswer_exam.url')),
    url('video_questions/', include('video_questions.url')),
    url('temp/',include('temp.url')),
    url('$',views.home)



]
