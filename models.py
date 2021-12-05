from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Departments(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=250)
 
    def get_name(self):
        return self.Name

    def get_description(self):
        return self.Description

    def __str__(self):
        return self.Name + '__' + self.Description

class  projects(models.Model):
    project_topic = models.CharField(max_length=50)
    project_title = models.CharField(max_length=50)
    submitted_by = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    project_file = models.FileField()
    Departments = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(projects):
        return projects.project_title + ' __ ' + projects.submitted_by + ' __ ' + projects.description

    def get_topic(self):
        return self.project_topic

    def get_name(self):
        return self.project_title

    def get_owner(self):
        return self.submitted_by

    def get_description(self):
        return self.description

    def get_file(self):
        self.project_file
    