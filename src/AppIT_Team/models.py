from django.db import models

# Models for AppIT_Team

class IT_Member(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    job_title=models.CharField(max_length=50) #dropdown
    is_staff=1 #TESTEAR

    def __str__(self):
        return f"IT Member: {self.first_name} {self.last_name} - {self.job_title}"