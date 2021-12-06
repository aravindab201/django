from django.db import models


# Create your models here.

class dept(models.Model):
    depid = models.IntegerField(max_length=10)
    depname = models.CharField(max_length=50)

    def __str__(self):
        return self.depname


class employee(models.Model):
    empid = models.CharField(max_length=100)
    empname = models.CharField(max_length=250)
    empaddress = models.CharField(max_length=250)
    depid = models.ForeignKey(dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.empname

