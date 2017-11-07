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


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('session_id', 'session_dt', 'admin', 'session_students')


class VerbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verb
        fields = ('verb_id', 'verb', 'definition', 'admin')


class AnimationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animation
        fields = ('animation_id', 'verb', 'image_address')


class VerbPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerbPack
        fields = ('verb_pack_id', 'title', 'admin', 'verb_pack_verbs', 'user_verb_packs')


class OwnedVerbPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerbPack
        fields = ('verb_pack_id', 'title', 'admin', 'verb_pack_verbs')


class LearnedVerbSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearnedVerb
        fields = ('learned_verb_id', 'verb', 'session', 'student', 'animations', 'created_dt', 'correct', 'tries')
