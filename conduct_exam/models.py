from django.db import models
from student_register.models import RegisterStudent
from teacher_register.models import TeacherRegister



# Create your models here.
class ConductExam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    exam_name = models.CharField(max_length=45)
    department = models.CharField(max_length=45)
    year = models.CharField(max_length=45)
    exam_date = models.DateField(blank=True, null=True)
    upload_question = models.CharField(max_length=45)
    # student_id = models.IntegerField(blank=True, null=True)
    student=models.ForeignKey(RegisterStudent,on_delete=models.CASCADE)

    # teacher_id = models.IntegerField(blank=True, null=True)
    teacher=models.ForeignKey(TeacherRegister,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'conduct_exam'

