from django.db import models
from .user import User
from .issue import Issue
from django.utils import timezone

class Comments(models.Model):
    commented_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='commented_by')
    issue_name=models.ForeignKey(Issue,on_delete=models.CASCADE)
    msg=models.CharField(max_length=200)
    mentions=models.ManyToManyField(User,related_name='mentions')
    Created_on=models.DateTimeField('date published',default=timezone.now)


    def __str__(self):
        return self.msg


