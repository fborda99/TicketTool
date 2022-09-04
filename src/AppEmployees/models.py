from django.db import models

# Models for AppEmployees

class Employee(models.Model):
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    job_title=models.CharField(max_length=50) 
    email=models.EmailField() #agregar leyenda de que el dominio es de la empresa
    workid=models.IntegerField() #agregar leyenda de que son 6 dígitos
    is_staff=0 

    def __str__(self):
        return f"Employee {self.work_id}: {self.first_name} {self.last_name} - {self.job_title}"
    
