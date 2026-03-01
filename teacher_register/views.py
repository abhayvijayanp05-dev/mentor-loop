from django.shortcuts import render
from teacher_register.models import TeacherRegister
from login.models import Login
# Create your views here.
def teacherRegister(request):
    if request.method=='POST':
        obj=TeacherRegister()
        obj.name=request.POST.get('teachername')
        obj.username=request.POST.get('username')
        obj.subject=request.POST.get('subject')
        obj.contact=request.POST.get('contact')
        obj.email=request.POST.get('email')
        obj.password=request.POST.get('password')
        obj.status='pending'

        obj.save()
        ob = Login()
        ob.username = obj.username
        ob.password = obj.password
        ob.u_id = obj.teacher_id
        ob.type = 'teacher'
        ob.save()


    return render(request,'teacher_register/teacherRegister.html')
def viewteacher(request):
    ob =TeacherRegister.objects.all()
    context = {
        'aa': ob
    }
    return render(request,'teacher_register/viewteacher.html',context)
def teacher_management(request):
    ob = TeacherRegister.objects.all()
    context = {
        'aa': ob
    }
    return render(request,'teacher_register/teacher_management.html',context)

def accept(request,idd):
    ob=TeacherRegister.objects.get(teacher_id=idd)
    ob.status='accepted'
    ob.save()

    return teacher_management(request)
def reject(request,idd):
    ob=TeacherRegister.objects.get(teacher_id=idd)
    ob.status='rejected'
    ob.save()

    return teacher_management(request)
def teacher_profile(request):
    ss = request.session['u_id']
    ob = TeacherRegister.objects.filter(teacher_id=ss)
    # ob =TeacherRegister.objects.all()
    context = {
        'aa': ob
    }
    return render(request,'teacher_register/teacher_profile.html',context)