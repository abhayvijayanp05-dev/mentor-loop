from django.db import models
from teacher_register.models import TeacherRegister
# Create your models here.
class Assignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    assignment_name = models.CharField(max_length=45)
    assignment_subject = models.CharField(max_length=45)
    assig_sublastdate = models.DateField()
    # teacher_id = models.IntegerField()
    teacher=models.ForeignKey(TeacherRegister,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'assignment'

