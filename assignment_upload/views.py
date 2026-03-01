from django.shortcuts import render
from assignment_upload.models import AssignmentUpload
import datetime
from  assignment.models import Assignment
from django.core.files.storage import FileSystemStorage
from teacher_register.models import TeacherRegister

# Create your views here.
def post_assignment(request):
    ss = request.session['u_id']
    obj=Assignment.objects.all()
    context={
        'k':obj
    }
    if request.method=='POST':
        obj=AssignmentUpload()

        obj.student_id=ss
       # obj.assignment_id=reques
        # obj.upload_assignment=request.POST.get('aaa')
        myfile=request.FILES['aaa']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.upload_assignment=myfile.name
        obj.assignment_id=request.POST.get('assignment_name')
        obj.upload_date=datetime.datetime.today()
        obj.save()
    return render(request,'assignment_upload/postassignment.html',context)
def viewassignmentteacher(request):
    ss = request.session['u_id']
    ob = AssignmentUpload.objects.filter(assignment__teacher_id=ss)
    # ob=AssignmentUpload.objects.all()
    context={
        'bb':ob
    }
    return render(request,'assignment_upload/viewAssignmentteacher.html',context)

def grade(request,idd):
    ob = AssignmentUpload.objects.get(fn_id=idd)
    context = {
        'bb': ob
    }
    if request.method=='POST':
        obj=AssignmentUpload.objects.get(fn_id=idd)
        obj.grade=request.POST.get('grade')

        obj.save()

    return render(request,'assignment_upload/grade.html',context)
from student_register.models import RegisterStudent
def viewgrade(request):
    ss = request.session['u_id']
    oo=RegisterStudent.objects.filter(student_id=ss).first()

    ob = AssignmentUpload.objects.filter(student_id=ss)
    # ob=AssignmentUpload.objects.all()
    context={
        'bb':ob
    }
    return render(request,'assignment_upload/viewgrade.html',context)
from parent_register.models import ParentRegister
def viewgradeparent(request):
    ss = request.session['u_id']
    ob=ParentRegister.objects.get(parent_id=ss)
    ob = AssignmentUpload.objects.filter(student_id=ob.student_id)
   # ob=AssignmentUpload.objects.all()
    context={
        'bb':ob
    }
    return render(request,'assignment_upload/pvg.html',context)
def viewteacher(request):
    ss = request.session['u_id']

    talist=list(Assignment.objects.filter(teacher_id=ss).values_list('assignment_id',flat=True))
    ob = AssignmentUpload.objects.filter(assignment_id__in=talist)
    # ob=AssignmentUpload.objects.filter()
    context={
        'bb':ob
    }
    return render(request,'assignment_upload/tvg.html',context)
def viewassignmentstudent(request):
    ss = request.session['u_id']
    ob = AssignmentUpload.objects.filter(student_id=ss)
    # ss = request.session['u_id']
    # teacher = TeacherRegister.objects.get(teacher_id=ss)
    # ob = AssignmentUpload.objects.filter(student_id=teacher.)
    # ob=AssignmentUpload.objects.all()
    context={
        'bb':ob
    }
    return render(request,'assignment_upload/viewAssignmentstudent.html',context)
def post_assignment_edit(request,idd):
    ob = AssignmentUpload.objects.get(fn_id=idd)
    ss = request.session['u_id']
    obf=Assignment.objects.all()
    context={
        's':ob,
        'k':obf
    }
    if request.method=='POST':
        obj = AssignmentUpload.objects.get(fn_id=idd)
        obj.student_id=ss
       # obj.assignment_id=reques
        # obj.upload_assignment=request.POST.get('aaa')
        myfile=request.FILES['aaa']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.upload_assignment=myfile.name
        obj.assignment_id=request.POST.get('assignment_name')
        obj.upload_date=datetime.datetime.today()
        obj.save()
    return render(request,'assignment_upload/postassignment_edit.html',context)
