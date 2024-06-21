from django.db import models

# Create your models here.

class Job(models.Model):
    job_name = models.CharField(max_length=255, unique=True)
    job_description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.job_name

class Crew(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    crew_name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.crew_name
    
    