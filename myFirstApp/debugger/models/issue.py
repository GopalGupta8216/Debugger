from django.db import models
from .project import Project
from .user import User
from django.utils import timezone

class Issue(models.Model):
    project_name=models.ForeignKey(Project,on_delete=models.CASCADE)
    reported_by=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=80,default='defect')
    heading=models.CharField(max_length=100)
    discription=models.CharField(max_length=200,default=' ')
    media_uploads=models.CharField(max_length=200,default=' ')
    reported_on=models.DateTimeField('date published',default=timezone.now)

    def __str__(self):
        return self.heading

