from django.db import models
from student_register.models import RegisterStudent


# Create your models here.
class ParentRegister(models.Model):
    parent_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    studentname = models.CharField(max_length=45)
    department = models.CharField(max_length=45)
    year = models.CharField(max_length=45)
    registernumber = models.CharField(max_length=45)
    contact = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    # studentusername = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    # student_id = models.IntegerField()
    student = models.ForeignKey(RegisterStudent, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'parent_register'

