from django.shortcuts import render
from feedback.models import Feedback
import datetime

# Create your views here.
def parentfeedback(request):
    ss = request.session['u_id']

    if request.method=='POST':
        obj=Feedback()
        obj.feedback=request.POST.get('feedback')
        obj.date=datetime.datetime.now()
        obj.parent_id=ss
        obj.save()
    return render(request,'feedback/parentfeedback.html')
from parent_register.models import ParentRegister
def view_feedback(request):
    ob = Feedback.objects.all()
    context = {
        'aa': ob
    }
    return render(request,'feedback/view_feedback.html',context)
from student_register.models import RegisterStudent
def view_feedback_teacher(request):
    ss = request.session['u_id']
    kk=RegisterStudent.objects.filter(teacher_id=ss).first()
    oo = ParentRegister.objects.filter(student_id=kk.student_id).first()
    ob = Feedback.objects.filter(parent_id=oo.parent_id)
    context = {
        'aa': ob
    }
    return render(request,'feedback/view_feedback_teacher.html',context)

