from . import models

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

	get_subjects_following= serializers.ReadOnlyField()

	class Meta:
		model = models.User
		fields = ('id', 'username', 'email','profile_picture', 'bio', 'first_name', 'last_name',
		'get_subjects_following')


class SubjectSerializer(serializers.ModelSerializer):

	get_lessons = serializers.ReadOnlyField()

	class Meta:
		model = models.Subject
		fields = ('id', 'name', 'get_lessons' )
		