from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from api.models import *

class LinkSerilizer(serializers.ModelSerializer):
    id = ReadOnlyField()
    visit_count = ReadOnlyField()

    class Meta:
        fields = "__all__"
        model = Link
    
class UserSerilizer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'])
        return user
    class Meta:
        model = User
        fields = ("first_name","last_name","username","password")
