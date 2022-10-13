from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Project(models.Model):
    projectName = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.projectName


class Client(models.Model):
    client_id = models.IntegerField()
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    clientProject = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name
