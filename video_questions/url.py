from django.conf.urls import url
from video_questions import views

urlpatterns = [
    url('add/', views.uploadvideo),
    url('view/', views.view_videos_and_questions),
    url('viewteacher/', views.view_videos_and_questions_teacher),
    url('att/', views.mark_attendance),
    url('edit/(?P<idd>\w+)', views.uploadvideo_edit),
    url('parent_attendance/',views.view_attendance_parent),
    url('teacher_attendance/',views.view_attendance_teacher)

]