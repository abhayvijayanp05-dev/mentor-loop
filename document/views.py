from django.shortcuts import render
from document.models import Document
from django.core.files.storage import FileSystemStorage
from student_register.models import RegisterStudent
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage


# Create your views here.
def upload_document(request):
    ss = request.session['u_id']
    if request.method == 'POST':
        obj = Document()
        obj.subject_name = request.POST.get('subjectname')
        obj.topic_name = request.POST.get('topicname')
        # obj.upload_document=request.POST.get('Uploaddocument')
        my_file = request.FILES['Uploaddocument']
        fs = FileSystemStorage()
        filename = fs.save(my_file.name, my_file)
        obj.upload_document = my_file.name
        obj.save()
        obj.teacher_id = ss
        obj.save()
    return render(request, 'document/upload_document.html')


def view_document(request):
    ss = request.session['u_id']
    student = RegisterStudent.objects.get(student_id=ss)
    ob = Document.objects.filter(teacher_id=student.teacher_id)
    # ob = Document.objects.all()
    context = {
        'aa': ob
    }
    return render(request, 'document/view_document.html', context)


def view_document_teacher(request):
    ss = request.session['u_id']
    ob = Document.objects.filter(teacher_id=ss)
    context = {
        'aa': ob
    }
    return render(request, 'document/view_document_teacher.html', context)


# def upload_document_edit(request, idd):
#     ss = request.session['u_id']
#     ob = Document.objects.get(teacher_id=ss)
#     context = {
#         'aa': ob
#     }
#     if request.method == 'POST':
#         obj = Document.objects.get(document_id=idd)
#         obj.subject_name = request.POST.get('subjectname')
#         obj.topic_name = request.POST.get('topicname')
#         # obj.upload_document=request.POST.get('Uploaddocument')
#         my_file = request.FILES['Uploaddocument']
#         fs = FileSystemStorage()
#         filename = fs.save(my_file.name, my_file)
#         obj.upload_document = my_file.name
#         obj.save()
#         obj.teacher_id = ss
#         obj.save()
#     return render(request, 'document/upload_document_edit.html', context)


def upload_document_edit(request, idd):
    ss = request.session['u_id']

    # Fetch the correct document using document_id
    ob = get_object_or_404(Document, document_id=idd, teacher_id=ss)

    if request.method == 'POST':
        ob.subject_name = request.POST.get('subjectname')
        ob.topic_name = request.POST.get('topicname')

        if 'Uploaddocument' in request.FILES:
            my_file = request.FILES['Uploaddocument']
            fs = FileSystemStorage()
            filename = fs.save(my_file.name, my_file)
            ob.upload_document = filename

        ob.save()

    context = {
        'aa': ob
    }

    return render(request, 'document/upload_document_edit.html', context)
