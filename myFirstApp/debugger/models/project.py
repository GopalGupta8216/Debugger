from django.db import models
from .user import User
from ckeditor.fields import RichTextField

class Project(models.Model):
    creator =models.ForeignKey(User,on_delete=models.CASCADE,related_name='creator')
    project_name = models.CharField(max_length=50)
    wiki = RichTextField(blank=True,null=True)
    team_member = models.ManyToManyField(User,related_name='team_member')

    def __str__(self):
        return self.project_name

