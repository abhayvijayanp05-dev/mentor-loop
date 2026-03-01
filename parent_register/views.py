from django.shortcuts import render
from parent_register .models import ParentRegister
from student_register.models import RegisterStudent
from login.models import Login
# Create your views here.
def registerparent(request):
    obj=RegisterStudent.objects.all()
    context={
        'k':obj
    }
    if request.method=='POST':
        obj=ParentRegister()
        obj.name=request.POST.get('Parentname')
        obj.username=request.POST.get('pusername')
        obj.studentname=request.POST.get('studentname')
        obj.studentusername=request.POST.get('susername')
        obj.department=request.POST.get('department')
        obj.year=request.POST.get('year1')
        obj.registernumber=request.POST.get('registerno')
        obj.contact=request.POST.get('scontact')
        obj.password=request.POST.get('spassword')
        obj.student_id=request.POST.get('ok')
        obj.status='pending'
        obj.save()

        ob=Login()
        ob.username=obj.username
        ob.password=obj.password
        ob.u_id=obj.parent_id
        ob.type='parent'
        ob.save()

    return render(request,'parent_register/registerparent.html',context)
def viewparent(request):
    ob=ParentRegister.objects.all()
    context={
        'aa':ob
    }
    return render(request,'parent_register/viewparent.html',context)
def parent_management(request):
    ob = ParentRegister.objects.all()
    context = {
        'bb': ob
    }
    return render(request,'parent_register/parent_management.html',context)
def accept(request,idd):
    ob=ParentRegister.objects.get(parent_id =idd)
    ob.status='accepted'
    ob.save()

    return parent_management(request)
def reject(request,idd):
    ob=ParentRegister.objects.get(parent_id =idd)
    ob.status='rejected'
    ob.save()

    return parent_management(request)
def viewparent(request):
    ob=ParentRegister.objects.all()
    context={
        'aa':ob
    }
    return render(request,'parent_register/viewparent.html',context)
def parent_profile(request):
    ss = request.session['u_id']
    ob = ParentRegister.objects.filter(parent_id=ss)
    # ob = ParentRegister.objects.all()
    context = {
        'aa': ob
    }
    return render(request,'parent_register/parent_profile.html',context)