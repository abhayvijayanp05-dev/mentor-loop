

# Create your views here.

from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect
from teacher_register.models import TeacherRegister
from parent_register.models import ParentRegister
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj=Login.objects.filter(username=username, password=password)

        tp = ""
        for ob in obj:
            tp = ob.type
            uid=ob.u_id
            if tp == "admin":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp == "student":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/student/')
            elif tp == "teacher":
                try:
                    org = TeacherRegister.objects.get(teacher_id=uid)
                    if org.status == 'accepted':
                        request.session["u_id"] = uid
                        return HttpResponseRedirect('/temp/teacher/')
                    else:
                        msg = 'your account not accepted'
                except TeacherRegister.DoesNotExist:
                    msg = 'account not found '
                return render(request, 'login/login.html', {'msg': msg})

            elif tp == "parent":
                # request.session["u_id"] = uid
                # return HttpResponseRedirect('/temp/parent/')
                try:
                    org = ParentRegister.objects.get(parent_id=uid)
                    if org.status == 'accepted':
                        request.session["u_id"] = uid
                        return HttpResponseRedirect('/temp/parent/')
                    else:
                        msg = 'your account not accepted'
                except TeacherRegister.DoesNotExist:
                    msg = 'account not found '
                return render(request, 'login/login.html', {'msg': msg})

        else:
                objlist = "username or password incorrect..... please try again..."
                context = {
                    'msg': objlist
                }
        return render(request, 'login/login.html',context)
    return render(request, 'login/login.html')