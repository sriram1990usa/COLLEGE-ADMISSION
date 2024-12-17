from django.db import models

# Create your models here.
class Courses(models.Model):
    name=models.CharField(max_length=200,null=True)
    duration=models.IntegerField(default=3,null=True,blank=True)
    fees=models.IntegerField(null=True,blank=True)
    decsription=models.CharField(null=True,blank=True,max_length=10000)
    def __str__(self):
        return str(self.name)