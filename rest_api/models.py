from django.core import exceptions
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# ----------------------validators------------------------
def validate_password(value):
    if len(value) < 7:
            raise ValidationError( _('minimum length must be 7'))
    

    
# -------------------validators-------------------------
        
# Create your models here.
class Advisor_details(models.Model):
    Advisor_name=models.CharField(max_length=50,default="")
    Advisor_Photo_URL=models.TextField(max_length=100000,default=1)
    
    def __str__(self):
        return self.Advisor_name
    
class User(models.Model):
    Name=models.CharField(max_length=100 ,blank=False)
    Email=models.EmailField(max_length=100,unique=True,blank=False)
    Password=models.CharField(max_length=50, validators=[validate_password])
       
    def __str__(self):
        return self.Name
    
class Book_call(models.Model):
    time=models.DateTimeField(blank=False)
    advisor_id=models.IntegerField(blank=False)
    user_id=models.IntegerField(blank=False)
    
    