from django.shortcuts import render
from complaint.models import Complaint

import datetime
# Create your views here.
def postcompaints(request):
    ss = request.session['u_id']
    if request.method=='POST':
        obj=Complaint()
        obj.complaint_categpry=request.POST.get('complaintcategory')
        obj.complaint_details=request.POST.get('complaintdetails')
        obj.student_id=ss
        # obj.teacher_id=1
        obj.date=datetime.datetime.today()

        obj.save()
    return render(request,'complaint/postcomplaints.html')
def replycomplaints(request,idd):
    ss = request.session['u_id']
    if request.method=='POST':
        obj=Complaint.objects.get(complaint_id=idd)

        obj.reply=request.POST.get('reply')
        # obj.teacher_id=1
        # obj.student_id=ss
        obj.save()
        return viewcomplaints(request)
    return render(request,'complaint/replycomplaints.html')
def viewcomplaints(request):
    ob = Complaint.objects.all()
    context = {
        'cc':ob
    }
    return render(request,'complaint/viewcomplaints.html',context)
def viewcomplaintsreply(request):
    ss=request.session['u_id']
    ob = Complaint.objects.filter(student_id=ss)
    context = {
        'dd': ob
    }
    return render(request,'complaint/viewcomplaintsreply.html',context)
def viewcomplaintsreplyadmin(request):

    ob = Complaint.objects.all()
    context = {
        'dd': ob
    }
    return render(request,'complaint/viewcomplaintsreplyadmin.html',context)