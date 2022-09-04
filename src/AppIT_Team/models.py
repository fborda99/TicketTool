from django.db import models
from django.contrib.auth.models import User

# Models for AppIT_Team
class IT_Member(models.Model):
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    jobtitle=models.CharField(max_length=50)
    is_staff=1 

    def __str__(self):
        return f"{self.name} {self.lastname} - {self.jobtitle}"

class Avatar(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="avatars",null=True,blank=True)
