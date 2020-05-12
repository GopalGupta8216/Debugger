from django.contrib import admin
from .models import Project,User,Issue,Comment

admin.site.register(Project)
admin.site.register(User)
admin.site.register(Issue)

admin.site.register(Comment)
# Register your models here.
