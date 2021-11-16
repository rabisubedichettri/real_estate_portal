from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=100, )
    password2 = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'gender', 'password1', 'password2', ]
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password1': {"write_only": True},
            'password2': {"write_only": True}}

    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 != password2:
            raise serializers.ValidationError('Passwords do not match.')
        return data

    def validate_password1(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    def validate_password2(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    def create(self, validated_data):
        instance = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            gender=validated_data['gender'],

        )
        instance.set_password(validated_data['password1'])
        instance.save()
        return instance

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=100)
    password1 = serializers.CharField(max_length=100)
    password2 = serializers.CharField(max_length=100)

    def validate_password1(self, value):
        password_validation.validate_password(value, self.instance)
        print("ok1")
        return value

    def validate_password2(self, value):
        password_validation.validate_password(value, self.instance)
        print("ok 2")
        return value

    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 != password2:
            raise serializers.ValidationError('Passwords do not match.')
        return data

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['gender','first_name','last_name']
