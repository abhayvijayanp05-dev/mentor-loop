from django.shortcuts import render
from student_register.models import RegisterStudent
from login.models import Login
from teacher_register.models import TeacherRegister
# Create your views here.
def Registerstudent(request):
    ss=request.session['u_id']
    if request.method=='POST':
        obj=RegisterStudent()
        obj.name=request.POST.get('studentname')
        obj.username=request.POST.get('susername')
        obj.department=request.POST.get('department')
        obj.year=request.POST.get('year')
        obj.registernumber=request.POST.get('registerno')
        obj.contact=request.POST.get('scontact')
        obj.email=request.POST.get('semail')
        obj.password=request.POST.get('spassword')
        obj.status='pending'
        obj.teacher_id=ss
        obj.save()
        ob = Login()
        ob.username = obj.username
        ob.password = obj.password
        ob.u_id = obj.student_id
        ob.type = 'student'
        ob.save()


    return render(request,'student_register/Registerstudent.html')

def viewstudent(request):
    ob = RegisterStudent.objects.all()
    context = {
        'aa': ob
    }
    return render(request,'student_register/viewstudent.html',context)
def student_management(request):
    ss=request.session['u_id']
    ob = RegisterStudent.objects.filter(teacher_id=ss)
    context = {
        'aa': ob
    }
    return render(request, 'student_register/student_management.html',context)

def edit(request,idd):
    obj=RegisterStudent.objects.get(student_id=idd)
    context={'k':obj}
    if request.method=='POST':
        obj=RegisterStudent.objects.get(student_id=idd)
        obj.name=request.POST.get('studentname')
        obj.username=request.POST.get('susername')
        obj.department=request.POST.get('department')
        obj.year=request.POST.get('year')
        obj.registernumber=request.POST.get('registerno')
        obj.contact=request.POST.get('scontact')
        obj.email=request.POST.get('semail')
        obj.password=request.POST.get('spassword')
        obj.status='pending'
        obj.save()
    return render(request,'student_register/edit.html',context)
def student_profile(request):
    ss = request.session['u_id']
    ob = RegisterStudent.objects.filter(student_id=ss)
    # ob = RegisterStudent.objects.all()
    context = {
        'aa': ob
    }
    return render(request,'student_register/student_pofile.html',context)
