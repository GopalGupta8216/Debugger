from rest_framework import serializers

from debugger.models import Issue
from .project_serializer import ProjectSerializer



class IssueSerializer(serializers.ModelSerializer):
    project_name = ProjectSerializer(many=True, read_only=True)
     
    class Meta:
        model = Issue
        fields = (
	'project_name',
	'reported_by',
	'status',
	' heading',
	'discription',
	'media_upload',
	'reported_on',
	'last_updated_on',
	'tag'
	)



