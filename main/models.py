from django.db import models

# Create your models here.
class Hospital (models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()


    def __str__(self):
        return self.name
    




class Patient (models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)


    def __str__(self):
        return self.first_name
    