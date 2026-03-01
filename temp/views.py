from django.shortcuts import render

# Create your views here.
def teacher(request):
    return render(request,'temp/teacher.html')
def student(request):
    return render(request,'temp/student.html')
def parent(request):
    return render(request,'temp/parent(home).html')
def admin(request):
    return render(request,'temp/admin.html')
def home(request):
    return render(request,'temp/home.html')

