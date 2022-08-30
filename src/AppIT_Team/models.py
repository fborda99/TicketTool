from django.db import models
# Models for AppIT_Team
class IT_Member(models.Model):
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    jobtitle=models.CharField(max_length=50)
    is_staff=1 #TESTEAR

    def __str__(self):
        return f"{self.name} {self.lastname} - {self.jobtitle}"