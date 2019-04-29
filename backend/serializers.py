from . import models

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.User
		fields = ('id', 'username', 'email','profile_picture', 'bio', 'first_name', 'last_name')
