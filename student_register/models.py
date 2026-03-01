from django.db import models
from teacher_register.models import TeacherRegister

# Create your models here.
class RegisterStudent(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    department = models.CharField(max_length=45)
    year = models.CharField(max_length=45)
    registernumber = models.CharField(max_length=45)
    contact = models.CharField(max_length=11)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    # teacher_id = models.IntegerField(blank=True, null=True)
    teacher = models.ForeignKey(TeacherRegister, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'register_student'

