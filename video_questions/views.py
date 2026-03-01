from django.shortcuts import render
from video_questions.models import VideoQuestions
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse
# Create your views here.
def uploadvideo(request):
    ss = request.session['u_id']
    if request.method=='POST':
        obj=VideoQuestions()
        obj.subjectname=request.POST.get('subjectname')
        obj.topicname=request.POST.get('topicname')
        # obj.uploadvideo=request.POST.get('video')

        my_file1 = request.FILES['video']
        fs = FileSystemStorage()
        filename = fs.save(my_file1.name, my_file1)
        obj.uploadvideo = my_file1.name


        # obj.uploadquestion=request.POST.get('questions')
        my_file = request.FILES['questions']
        fs = FileSystemStorage()
        filename = fs.save(my_file.name, my_file)
        obj.uploadquestion = my_file.name
        obj.teacher_id=ss
        obj.duration=request.POST.get('dd')
        obj.save()

    return render(request,'video_questions/uploadvideo.html')
from student_register.models import RegisterStudent
# def view_videos_and_questions(request):
#     ss = request.session['u_id']
#     oj=RegisterStudent.objects.get(student_id=ss)
#     ob = VideoQuestions.objects.filter(teacher_id=oj.teacher_id)
#     context = {
#         'aa': ob
#     }
#     return render(request,'video_questions/view_videos_and_questions.html',context)

import math
from django.db.models import Count

def view_videos_and_questions(request):

    ss = request.session['u_id']
    oj = RegisterStudent.objects.get(student_id=ss)

    videos = VideoQuestions.objects.filter(teacher_id=oj.teacher_id)

    video_data = []

    for video in videos:

        # assume you store video duration in seconds in DB
        duration_seconds = video.duration   # add this field in model

        total_intervals = math.floor(duration_seconds / 300)

        attended_intervals = Attendance.objects.filter(
            video_id=video.video_id,
            student_id=ss
        ).count()

        if total_intervals > 0:
            percentage = (attended_intervals / total_intervals) * 100
        else:
            percentage = 0

        video_data.append({
            "video": video,
            "attendance_percentage": round(percentage, 2)
        })

    context = {"videos": video_data}

    return render(request,'video_questions/view_videos_and_questions.html',context)
def view_videos_and_questions_teacher(request):
    ss=request.session['u_id']
    ob = VideoQuestions.objects.filter(teacher_id=ss)
    context = {
        'aa': ob
    }
    return render(request,'video_questions/view_videos_and_questions_teacher.html',context)
def uploadvideo_edit(request,idd):
    ob = VideoQuestions.objects.get(video_id=idd)
    # ob = VideoQuestions.objects.all()
    context = {
        'k': ob
    }
    ss = request.session['u_id']
    if request.method=='POST':
        obj = VideoQuestions.objects.get(video_id=idd)
        obj.subjectname=request.POST.get('subjectname')
        obj.topicname=request.POST.get('topicname')
        # obj.uploadvideo=request.POST.get('video')

        my_file1 = request.FILES['video']
        fs = FileSystemStorage()
        filename = fs.save(my_file1.name, my_file1)
        obj.uploadvideo = my_file1.name


        # obj.uploadquestion=request.POST.get('questions')
        my_file = request.FILES['questions']
        fs = FileSystemStorage()
        filename = fs.save(my_file.name, my_file)
        obj.uploadquestion = my_file.name
        obj.teacher_id=ss
        obj.duration = request.POST.get('dd')
        # obj.student_id=1
        obj.save()

    return render(request,'video_questions/uploadvideoedit.html',context)

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from datetime import datetime
from .models import Attendance
#
# @csrf_exempt
# def mark_attendance(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#
#         video_id = data.get("video_id")
#         student_id = request.session.get('u_id')
#
#         if not student_id:
#             return JsonResponse({"status": "no session"})
#
#         Attendance.objects.create(
#             video_id=video_id,
#             student_id=student_id,
#             date=datetime.now().date(),
#             time=datetime.now().time()
#         )
#
#         return JsonResponse({"status": "success"})
#
#     return JsonResponse({"status": "failed"})
#



@csrf_exempt
def mark_attendance(request):
    if request.method == "POST":
        data = json.loads(request.body)

        video_id = data.get("video_id")
        interval_number = data.get("interval_number")
        student_id = request.session.get('u_id')

        Attendance.objects.get_or_create(
            video_id=video_id,
            student_id=student_id,
            interval_number=interval_number,
            date=datetime.now().date(),
            defaults={'time': datetime.now().time()}
        )

        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "failed"})

# from parent_register.models import ParentRegister
# def view_attendance_parent(request):
#     ss = request.session['u_id']
#     oj = ParentRegister.objects.get(parent_id=ss)
#     ll=RegisterStudent.objects.filter(parent_id=oj.parent_id).first
#     videos = VideoQuestions.objects.filter(teacher_id=ll.teacher_id)
#
#     video_data = []
#
#     for video in videos:
#
#         # assume you store video duration in seconds in DB
#         duration_seconds = video.duration  # add this field in model
#
#         total_intervals = math.floor(duration_seconds / 300)
#
#         attended_intervals = Attendance.objects.filter(
#             video_id=video.video_id,
#             student_id=ss
#         ).count()
#
#         if total_intervals > 0:
#             percentage = (attended_intervals / total_intervals) * 100
#         else:
#             percentage = 0
#
#         video_data.append({
#             "video": video,
#             "attendance_percentage": round(percentage, 2)
#         })
#
#     context = {"videos": video_data}
#
#     return render(request,'video_questions/view_attendance_parent.html',context)

import math
from parent_register.models import ParentRegister

import math
from parent_register.models import ParentRegister

def view_attendance_parent(request):

    parent_id = request.session['u_id']

    parent = ParentRegister.objects.get(parent_id=parent_id)

    # ✅ FIXED: parent contains student_id
    student = RegisterStudent.objects.get(student_id=parent.student_id)

    videos = VideoQuestions.objects.filter(teacher_id=student.teacher_id)

    video_data = []

    for video in videos:

        duration_seconds = video.duration if video.duration else 0

        total_intervals = math.floor(duration_seconds / 300)

        attended_intervals = Attendance.objects.filter(
            video_id=video.video_id,
            student_id=student.student_id
        ).count()

        if total_intervals > 0:
            percentage = (attended_intervals / total_intervals) * 100
        else:
            percentage = 0

        video_data.append({
            "video": video,
            "attendance_percentage": round(percentage, 2)
        })

    context = {"videos": video_data}

    return render(request, 'video_questions/view_attendance_parent.html', context)
# def view_attendance_teacher(request):
#     ss=request.session['u_id']
#     ob = VideoQuestions.objects.filter(teacher_id=ss)
#     context = {
#         'aa': ob
#     }
#     return render(request,'video_questions/view_attendance_teacher.html',context)

import math

def view_attendance_teacher(request):

    teacher_id = request.session['u_id']

    # Get teacher videos
    videos = VideoQuestions.objects.filter(teacher_id=teacher_id)

    # Get students under this teacher
    students = RegisterStudent.objects.filter(teacher_id=teacher_id)

    data = []

    for student in students:

        student_videos = []

        for video in videos:

            duration_seconds = video.duration if video.duration else 0
            total_intervals = math.floor(duration_seconds / 300)

            attended_intervals = Attendance.objects.filter(
                video_id=video.video_id,
                student_id=student.student_id
            ).count()

            if total_intervals > 0:
                percentage = (attended_intervals / total_intervals) * 100
            else:
                percentage = 0

            student_videos.append({
                "video": video,
                "attendance_percentage": round(percentage, 2)
            })

        data.append({
            "student": student,
            "videos": student_videos
        })

    context = {"data": data}

    return render(request, 'video_questions/view_attendance_teacher.html', context)