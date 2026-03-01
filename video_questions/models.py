from django.db import models
from student_register.models import RegisterStudent
from teacher_register.models import TeacherRegister

# Create your models here.
class VideoQuestions(models.Model):
    video_id = models.AutoField(primary_key=True)
    subjectname = models.CharField(max_length=45)
    topicname = models.CharField(max_length=45)
    uploadvideo = models.CharField(max_length=1000)
    uploadquestion = models.CharField(max_length=45)
    # teacher_id = models.IntegerField()
    teacher=models.ForeignKey(TeacherRegister,on_delete=models.CASCADE)
    duration= models.IntegerField(blank=True, null=True)
    # student=models.ForeignKey(RegisterStudent,on_delete=models.CASCADE)


    class Meta:
        managed = False
        db_table = 'video_questions'


class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    video_id = models.IntegerField(blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    interval_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance'

