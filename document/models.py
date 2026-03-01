from django.db import models
from teacher_register.models import TeacherRegister
from student_register.models import RegisterStudent

# Create your models here.
class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(db_column=' subject_name', max_length=45)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    topic_name = models.CharField(max_length=45)
    upload_document = models.CharField(max_length=1000)
    # teacher_id = models.IntegerField()
    teacher=models.ForeignKey(TeacherRegister,on_delete=models.CASCADE)
    # student_id = models.IntegerField(blank=True, null=True)
    student=models.ForeignKey(RegisterStudent,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'document'
