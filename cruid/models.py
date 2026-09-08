from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=200)
    uniq_id = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    feald = models.TextField(blank=True)
    
    def __str__(self):
       return self.uniq_id