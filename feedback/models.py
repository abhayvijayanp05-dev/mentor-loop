from django.db import models
from parent_register.models import ParentRegister
from student_register.models import RegisterStudent

# Create your models here.
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    feedback = models.CharField(max_length=45)
    # parent_id = models.IntegerField()
    parent=models.ForeignKey(ParentRegister,on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'feedback'

