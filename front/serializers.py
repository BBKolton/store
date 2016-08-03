from django.forms import widgets
from rest_framework import serializers
class UsersSerializer(serializers.ModelSerializer):
 created = serializers.DateTimeField()
 username = serializers.CharField(max_length=10)
 fname = serializers.CharField(max_length=200)
 lname = serializers.CharField(max_length=200)
 user_type = serializers.ChoiceField(choices=USER_CHOICES)
def create(self, validated_data):
 """
 Create and return a new `Users` instance, given the validated data.
 """
 return Users.objects.create(**validated_data)
def update(self, instance, validated_data):
 """
 Update and return an existing `Users` instance, given the validated data.
 """
 instance.created = validated_data.get('created', instance.created)
 instance.username = validated_data.get('username', instance.username)
 instance.fname = validated_data.get('fname', instance.fname)
 instance.lname = validated_data.get('lname', instance.lname)
 instance.user_type = validated_data.get('user_type', instance.user_type)
 instance.save()
 return instance
