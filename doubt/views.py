from django.shortcuts import render
from doubt.models import Doubt
import datetime
# Create your views here.
def post_doubts(request):
    ss = request.session['u_id']
    if request.method=='POST':
        obj=Doubt()
        obj.subject_name=request.POST.get('subjectname')
        obj.topic_name=request.POST.get('topicname')
        obj.upload_doubt=request.POST.get('message')
        obj.date=datetime.datetime.today()
        # obj.teacher_id=ss
        obj.student_id=ss
        obj.save()
    return render(request,'doubt/post_doubts.html')
def reply_for_doubts(request,idd):
    # ss = request.session['u_id']
    ob = Doubt.objects.get(doubt_id=idd)
    context = {
        'aa': ob
    }

    if request.method=='POST':
        obj=Doubt.objects.get(doubt_id=idd)
        # obj.student_question=request.POST.get('question')
        obj.reply=request.POST.get('reply')
        # obj.date=datetime.datetime.today()
        # obj.student_id=ss
        # obj.teacher_id=ss
        obj.save()
        return view_doubt(request)
    return render(request,'doubt/reply_for_doubts.html',context)
def view_doubt(request):
    ss = request.session['u_id']
    ob = Doubt.objects.filter(student__teacher_id=ss)

    # ob = Doubt.objects.all()
    context = {
        'aa': ob
    }
    return render(request,'doubt/view_doubt.html',context)
def view_reply(request):
    ss = request.session['u_id']
    ob = Doubt.objects.filter(student_id=ss)

    # ob = Doubt.objects.all()
    context = {
        'bb': ob
    }
    return render(request,'doubt/view_reply.html',context)
def view_reply_teacher(request):
    ss = request.session['u_id']
    ob = Doubt.objects.filter(student__teacher_id=ss)
    context = {
        'bb': ob
    }
    return render(request,'doubt/view_reply_teacher.html',context)

