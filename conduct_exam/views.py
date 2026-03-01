from django.shortcuts import render
from conduct_exam.models import ConductExam
from django.core.files.storage import FileSystemStorage
import datetime
# Create your views here.
def conductexam(request):
    ss=request.session['u_id']
    if request.method=='POST':
        obj=ConductExam()
        obj.department=request.POST.get('department')
        obj.exam_name=request.POST.get('examtname')
        obj.year=request.POST.get('year')
        obj.exam_date=datetime.datetime.today()
        obj.teacher_id=ss
        obj.save()
    return render(request,'conduct_exam/conductexam.html')
def examquestion(request,idd):
    ss = request.session['u_id']
    if request.method=='POST':
        obj=ConductExam.objects.get(exam_id=idd)
        obj.teacher_id=ss
        # obj.exam_name=request.POST.get('examname')
        # obj.upload_question=request.POST.get('examquestion')
        my_file = request.FILES['examquestion']
        fs=FileSystemStorage()
        filename=fs.save(my_file.name,my_file)
        obj.upload_question = my_file.name
        obj.save()
    return render(request,'conduct_exam/examquestion.html')
def view_conduct_exam(request):
    # ss = request.session['u_id']
    # ob = ConductExam.objects.filter(teacher_id=ss)
    ss = request.session['u_id']
    student = RegisterStudent.objects.get(student_id=ss)
    ob = ConductExam.objects.filter(teacher_id=student.teacher_id)
    # ob = ConductExam.objects.all()

    context = {
        'ee': ob
    }
    return render(request,'conduct_exam/view_conduct_exam.html',context)
from student_register.models import RegisterStudent
def view_conduct_exam_student(request):
    ss = request.session['u_id']
    student = RegisterStudent.objects.get(student_id=ss)
    ob = ConductExam.objects.filter(teacher_id=student.teacher_id)
    # ob = ConductExam.objects.all()
    context = {
        'ff': ob
    }
    return render(request,'conduct_exam/view_conduct_exam_student.html',context)
def view_conduct_exam_teacher(request):
    ss = request.session['u_id']
    ob = ConductExam.objects.filter(teacher_id=ss)
    # ob = ConductExam.objects.all()
    context = {
        'ff': ob
    }
    return render(request,'conduct_exam/view_conduct_exam_teacher.html',context)
def view_exam_teacher(request):
    ss = request.session['u_id']
    ob = ConductExam.objects.filter(teacher_id=ss)
    # ob = ConductExam.objects.all()
    context = {
        'ee': ob
    }
    return render(request,'conduct_exam/view_exam_teacher.html',context)
