from django.db import models
from student_register.models import RegisterStudent
# Create your models here.
class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    # student_id = models.IntegerField()
    student=models.ForeignKey(RegisterStudent,on_delete=models.CASCADE)
    complaint_categpry = models.CharField(max_length=45)
    complaint_details = models.CharField(max_length=45)
    reply = models.CharField(max_length=45)
    teacher_id = models.CharField(max_length=45)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'complaint'

