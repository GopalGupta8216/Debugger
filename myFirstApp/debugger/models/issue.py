from django.db import models
from .project import Project
from .user import User
from django.utils import timezone

TAG_CHOICES = ( 
    ("1","design"), 
    ("2","dev"), 
    ("3","UI"), 
    ("4","Ux"), 
 
)
STATUS_CHOICES = (
        ("1","reported"),
    ("2","checked"),
    ("3","solved"),
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
    assigned_to = models.ForeignKey(
     User, 
     on_delete = models.CASCADE,
     related_name='assigned_by',
     default=' '
     )
    assigned_to = models.ForeignKey(
    User,
    on_delete = models.CASCADE,
    related_name='assigned_to',
    default=' '
    )

    def __str__(self):
        return self.heading

