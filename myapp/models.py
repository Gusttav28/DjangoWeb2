from django.db import models

# Create your models here.

class project(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Task(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    Project = models.ForeignKey(project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.Title + '-' + self.Project.name
            