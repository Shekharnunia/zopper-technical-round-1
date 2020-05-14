from rest_framework import serializers
from accounts.models import User


class AccountCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = (
            "email",
            "password",
        )
        write_only_fields = ("password",)


class UserListSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = [
			"id",
			"email",
			"first_name",
			"last_name",
			"avatar",
		]