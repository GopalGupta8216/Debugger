from django.db import models
from .project import Project
from .user import User
from django.utils import timezone

TAG_CHOICES = ( 
    ("design", "1"), 
    ("dev", "2"), 
    ("UI", "3"), 
    ("Ux", "4"), 
 
)
STATUS_CHOICES = (
        ("reported", "1"),
    ("checked", "2"),
    ("solved", "3"),
)
class Issue(models.Model):
    project_name = models.ForeignKey(
    Project,
    on_delete = models.CASCADE
    )
    reported_by = models.ForeignKey(
    User,
    on_delete = models.CASCADE
    )
    status = models.CharField(
    max_length = 80,
    default = 'reported',
    choices = STATUS_CHOICES
    )
    heading = models.CharField(
    max_length = 100 
    )
    discription = models.CharField(
    max_length = 200,
    default = ' '
    )
    media_upload = models.CharField(
    max_length = 200,
    default=' '
    )
    reported_on = models.DateTimeField(
    'date published',
     auto_now=True,
     null = True
     )
    last_updated_on=models.DateTimeField(
    'Last Updated On',
    auto_now_add=True,
    null = True
    )
    tag = models.CharField(
    max_length = 20,
    choices = TAG_CHOICES,
    default = 'dev'
    )
    def __str__(self):
        return self.heading

