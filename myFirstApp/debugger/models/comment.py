from django.db import models
from .user import User
from .issue import Issue
from django.utils import timezone

class Comment(models.Model):
    commented_by = models.ForeignKey(
    User,on_delete = models.CASCADE,
    related_name = 'commented_by'
    )

    issue_name = models.ForeignKey(
    Issue,
    on_delete = models.CASCADE
    )

    message = models.CharField(
    max_length = 200
    )

    mention = models.ManyToManyField( 
    User,
    related_name='mentions'
        )
    created_on = models.DateTimeField('date published',auto_now_add=True)


    def __str__(self):
        return self.message


