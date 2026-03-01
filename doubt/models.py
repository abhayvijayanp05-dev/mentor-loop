from django.db import models

from teacher_register.models import TeacherRegister
from student_register.models import RegisterStudent
# Create your models here.
class Doubt(models.Model):
    doubt_id = models.AutoField(primary_key=True)
    # student_id = models.IntegerField()
    student=models.ForeignKey(RegisterStudent,on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=45)
    topic_name = models.CharField(max_length=45)
    upload_doubt = models.CharField(max_length=45)
    student_question = models.CharField(max_length=45)
    reply = models.CharField(max_length=45)
    # teacher_id = models.IntegerField()
    teacher=models.ForeignKey(TeacherRegister,on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doubt'



