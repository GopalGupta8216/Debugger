from rest_framework import serializers


from debugger.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('enrollment','name','image','email','is_admin')

