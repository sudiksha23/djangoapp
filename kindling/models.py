from django.db import models
#from PIL import Image

# Create your models here.

class EntrySignup(models.Model):
   # details=models.ForeignKey(Details, on_delete=models.CASCADE)
    uname=models.CharField(max_length=122, primary_key=True)
    psw=models.CharField(max_length=122)
    fname=models.CharField(max_length=122)
    lname=models.CharField(max_length=122)
    country=models.CharField(max_length=122)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=100)
    zipp=models.IntegerField()
    gender=models.CharField(max_length=10)
    interested_in=models.CharField(max_length=10)
    marital_status=models.CharField(max_length=15)
    religion=models.CharField(max_length=20)
    occupation=models.CharField(max_length=30)
    education_status=models.CharField(max_length=20)
    subject=models.TextField()
    dob=models.DateField()
    dp = models.ImageField(upload_to='media', blank=True, null=True, verbose_name="", default='img.jpg')
    
    def __str__(self):
        return self.uname

    

    