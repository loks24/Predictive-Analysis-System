from django.db import models
import csv


class GetTagCode(models.Model):
    
    TagCode=models.CharField(max_length=20)
    Labels=models.CharField(max_length=20)
    

    class Meta:
        
        
        db_table='final'
    
    def __str__(self):
        return str(self.Labels)
   

class Report(models.Model):

    TagCode=models.CharField(max_length=20)
    CurrentValue=models.CharField(max_length=20)
    MinValue=models.CharField(max_length=20)
    MaxValue=models.CharField(max_length=20)
    MinTime=models.CharField(max_length=20)
    MaxTime=models.CharField(max_length=20)
    HourTime=models.CharField(max_length=20)
    Name=models.CharField(max_length=20)
    


    class Meta:

        db_table='report'
        

    def __str__(self):
        
        return str(self.TagCode)




