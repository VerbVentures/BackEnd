from rest_framework import serializers

from api.models import (
    VerbVentureUser,
    Admin,
    Student,
    Session,
    Verb,
    Animation,
    VerbPack,
    LearnedVerb
)
class VerbVentureUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerbVentureUser
        fields = ('user_id', 'first_name', 'last_name')

class AdminSerializer(serializers.ModelSerializer):
    user = VerbVentureUserSerializer()

    class Meta:
        model = Admin
        fields = ('admin_id', 'user', 'email', 'phone_number')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = VerbVentureUser.objects.create(**user_data)
        admin = Admin.objects.create(user=user, **validated_data)
        return admin

class StudentSerializer(serializers.ModelSerializer):
    user = VerbVentureUserSerializer()
    class Meta:
        model = Student
        fields = ('student_id', 'user', 'admin')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = VerbVentureUser.objects.create(**user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student


class Session(serializers.ModelSerializer):
    pass


class Verb(serializers.ModelSerializer):
    pass

class Animation(serializers.ModelSerializer):
    pass


class VerbPack(serializers.ModelSerializer):
    pass


class LearnedVerb(serializers.ModelSerializer):
    pass
