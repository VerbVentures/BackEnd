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
        fields = ('userId', 'firstName', 'lastName')


class AdminSerializer(serializers.ModelSerializer):
    user = VerbVentureUserSerializer()

    class Meta:
        model = Admin
        fields = ('accountKitId', 'email', 'user')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = VerbVentureUser.objects.create(**user_data)
        admin = Admin.objects.create(user=user, **validated_data)
        return admin


class StudentSerializer(serializers.ModelSerializer):
    user = VerbVentureUserSerializer()
    class Meta:
        model = Student
        fields = ('studentId', 'user', 'admin')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = VerbVentureUser.objects.create(**user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student


    def update(self, instance, validated_data):
        instance.admin = validated_data['admin']
        instance.user.firstName = validated_data['user']['firstName']
        instance.user.lastName = validated_data['user']['lastName']
        instance.user.save()
        instance.save()

        return instance


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('sessionId', 'sessionDt', 'admin', 'sessionStudents')


class VerbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verb
        fields = ('verbId', 'verb', 'definition', 'admin')


class AnimationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animation
        fields = ('animationId', 'verb', 'imageAddress')


class VerbPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerbPack
        fields = ('verbPackId', 'title', 'admin', 'verbPackVerbs', 'userVerbPacks')


class OwnedVerbPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerbPack
        fields = ('verbPackId', 'title', 'admin', 'verbPackVerbs')


class LearnedVerbSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearnedVerb
        fields = ('learnedVerbId', 'verb', 'session', 'student', 'animations', 'createdDt', 'correct', 'tries')
