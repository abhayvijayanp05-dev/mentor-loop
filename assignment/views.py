from django.shortcuts import render
from assignment.models import Assignment
import datetime
# Create your views here.
def add_assignment(request):
    ss=request.session['u_id']
    if request.method=='POST':
        obj=Assignment()
        obj.assig_sublastdate=datetime.datetime.today()
        obj.assignment_name=request.POST.get('assignmentname')
        obj.assignment_subject=request.POST.get('assignmentsubject')
        obj.teacher_id=ss
        obj.save()

    return render(request,'assignment/addassignment.html')
from student_register.models import RegisterStudent
def viewassignment(request):
    ss = request.session['u_id']
    student = RegisterStudent.objects.get(student_id=ss)
    ob = Assignment.objects.filter(teacher_id=student.teacher_id)
    # ss = request.session['u_id']
    # ob = Assignment.objects.filter(teacher_id=ss)
    # ob=Assignment.objects.all()
    context={
        'aa':ob
    }
    return render(request,'assignment/viewassignments.html',context)
def viewassignment_teacher(request):
    ss = request.session['u_id']
    ob=Assignment.objects.filter(teacher_id=ss)
    context={
        'aa':ob
    }
    return render(request,'assignment/viewassignments_teacher.html',context)