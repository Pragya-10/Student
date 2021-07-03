from django.db import models

class Employee(models.Model):
    eid = models.CharField(max_length = 20)
    ename = models.CharField(max_length=100)
    eclass = models.CharField(max_length=100,null=True,blank=False)
    eemail = models.CharField(max_length=50)
    econtact = models.CharField(max_length = 30)


