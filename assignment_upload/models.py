from django.db import models
from assignment.models import Assignment
from student_register.models import RegisterStudent
from teacher_register.models import TeacherRegister
# Create your models here.
class AssignmentUpload(models.Model):
    fn_id = models.AutoField(primary_key=True)
    # assignment_id = models.IntegerField()
    assignment=models.ForeignKey(Assignment,on_delete=models.CASCADE)
    # student_id = models.IntegerField()
    student=models.ForeignKey(RegisterStudent,on_delete=models.CASCADE)
    upload_assignment = models.CharField(max_length=45)
    upload_date = models.DateField()
    grade = models.CharField(max_length=45)


    class Meta:
        managed = False
        db_table = 'assignment_upload'
