from django.db import models
from .user import User
from .issue import Issue

class Issue_assigned(models.Model):
    assigned_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='assigned_by')
    assigned_to=models.ForeignKey(User,on_delete=models.CASCADE,related_name='assigned_to')
    issue_name=models.OneToOneField(Issue,on_delete=models.CASCADE,primary_key=True)

