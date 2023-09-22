from django.db import models

# Create your models here.

class UserAccount(models.Model):
    track = models.CharField(max_length=200, default="")

    name = models.CharField(max_length=200, default="")
    leader = models.CharField(max_length=200, default="")
    email = models.CharField( max_length=254 , default="")
    phone = models.CharField(max_length=12 , default="")
    

    City = models.CharField( max_length=50, default = "")
    state= models.CharField( max_length=50, default = "")
    
    profession = models.CharField( max_length=50, default = "")
    organisation = models.CharField( max_length=50, default = "", null=True)
    referral = models.CharField( max_length=50, default = "")

   

    def __str__(self):
        return self.name
    
class UserMessage(models.Model):
     name = models.CharField(max_length=200, default="")
     email = models.CharField( max_length=254 , default="")
     phone = models.CharField(max_length=12 , default="")
     message = models.CharField( max_length=50, default = "")

   

     def __str__(self):
        return self.name