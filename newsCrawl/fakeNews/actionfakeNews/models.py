from django.db import models

# Create your models here.
class Fake_NEWS(models.Model):
    link =  models.CharField(max_length= 500,blank = False)
    
    def __str__(self):
        return self.link
    
class Authenticate_NEWS(models.Model):
    link =  models.CharField(max_length= 500,blank = False)
    
    def __str__(self):
        return self.link