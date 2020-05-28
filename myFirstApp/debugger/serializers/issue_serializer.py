from rest_framework import serializers

from debugger.models import Issue,User





class IssueSerializer(serializers.ModelSerializer):
    assigned_by=serializers.SlugRelatedField(many=False,slug_field='name',queryset=User.objects.all())
    assigned_to=serializers.SlugRelatedField(many=False,slug_field='name',queryset=User.objects.all())
	#reported_by=serializers.SlugRelatedField(many=False,slug_field='name',queryset=User.objects.all()) 
    class Meta:
        model = Issue
        fields = ('project_name','reported_by',	'status','heading', 'discription', 'media_upload', 'reported_on', 'last_updated_on', 'tag', 'assigned_to', 'assigned_by')


class IssueUpdateSerializer(serializers.ModelSerializer):
    assigned_by=serializers.SlugRelatedField(many=False,slug_field='name',queryset=User.objects.all())
    assigned_to=serializers.SlugRelatedField(many=False,slug_field='name',queryset=User.objects.all())
	#reported_by=serializers.SlugRelatedField(many=False,slug_field='name',queryset=User.objects.all()) 
    heading = serializers.ReadOnlyField()
    discription = serializers.ReadOnlyField()

    class Meta:
        model = Issue
        fields = ('project_name','reported_by',	'status','heading', 'discription', 'media_upload', 'reported_on', 'last_updated_on', 'tag', 'assigned_to', 'assigned_by')