from rest_framework import serializers

from debugger.models import Issue,User





class IssueSerializer(serializers.ModelSerializer):
    assigned_by=serializers.RelatedField(source='User', read_only=True)
    assigned_to=serializers.RelatedField(source='User', read_only=True)

     
    class Meta:
        model = Issue
        fields = (
	'project_name',
	'reported_by',
	'status',
	'heading',
	'discription',
	'media_upload',
	'reported_on',
	'last_updated_on',
	'tag',
        'assigned_to',
        'assigned_by'
	)



