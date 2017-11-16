from random import randint, shuffle
from django.http import Http404
from django.db.models import Q
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
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
from api.serializers import (
    VerbVentureUserSerializer,
    AdminSerializer,
    StudentSerializer,
    SessionSerializer,
    VerbSerializer,
    AnimationSerializer,
    VerbPackSerializer,
    LearnedVerbSerializer,
    OwnedVerbPackSerializer
)

class VerbVentureUserList(generics.ListAPIView):
    queryset = VerbVentureUser.objects.all()
    serializer_class = VerbVentureUserSerializer


class AdminListCreate(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class AdminRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentList(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        admin = self.kwargs['pk']
        return Student.objects.filter(admin=admin)


class VerbList(generics.ListAPIView):
    serializer_class = VerbSerializer

    def get_queryset(self):
        admin = self.kwargs['pk']
        return Verb.objects.filter(Q(admin=admin) | Q(admin=None))


class VerbPackList(generics.ListAPIView):
    serializer_class = OwnedVerbPackSerializer

    def get_queryset(self):
        user = self.kwargs['pk']
        return VerbPack.objects.filter(user_verb_packs=user)


class VerbPackListAdmin(generics.ListAPIView):
    serializer_class = OwnedVerbPackSerializer

    def get_queryset(self):
        admin = self.kwargs['pk']
        return VerbPack.objects.filter(admin=admin)


class SessionList(generics.ListAPIView):
    serializer_class = SessionSerializer

    def get_queryset(self):
        admin = self.kwargs['pk']
        return Session.objects.filter(admin=admin)


class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SessionListCreate(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class VerbListCreate(generics.ListCreateAPIView):
    queryset = Verb.objects.all()
    serializer_class = VerbSerializer


class VerbRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Verb.objects.all()
    serializer_class = VerbSerializer


class AnimationListCreate(generics.ListCreateAPIView):
    queryset = Animation.objects.all()
    serializer_class = AnimationSerializer


class AnimationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animation.objects.all()
    serializer_class = AnimationSerializer


class VerbPackListCreate(generics.ListCreateAPIView):
    queryset = VerbPack.objects.all()
    serializer_class = VerbPackSerializer


class VerbPackRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = VerbPack.objects.all()
    serializer_class = VerbPackSerializer


class LearnedVerbListCreate(generics.ListCreateAPIView):
    queryset = LearnedVerb.objects.all()
    serializer_class = LearnedVerbSerializer


class LearnedVerbRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = LearnedVerb.objects.all()
    serializer_class = LearnedVerbSerializer


class GetRandomVerb(APIView):

    def get(self, request, pk, format=None):
        # get student
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

        # get student's verbpacks
        userId = student.user.userId
        user_verb_packs = VerbPack.objects.filter(userVerbPacks__pk=userId)

        # get list of unique verbs in all of students verbpacks
        all_verbs = Verb.objects.none()
        for verbpack in user_verb_packs:
            verbs = verbpack.verbPackVerbs.all()
            all_verbs = all_verbs | verbs

        # randomly pick one verb
        all_verbs_list = list(all_verbs)
        print(all_verbs_list)
        shuffle(all_verbs_list)
        selected_verb = all_verbs_list[0]
        print(selected_verb)

        # get one correct annimation
        correct_animations = list(Animation.objects.filter(verb=selected_verb))
        shuffle(correct_animations)
        correct_animation = correct_animations[0]
        print(correct_animation)

        # ranomly pick 3 other incorrect animations
        all_other_animations = list(Animation.objects.exclude(verb=selected_verb))
        shuffle(all_other_animations)
        invalid_animations = all_other_animations[:3]
        print(invalid_animations)

        # return JSON object
        response_dict = {}
        verb_dict = {
            'verbId': selected_verb.verbId,
            'verb': selected_verb.verb,
            'definition': selected_verb.definition

        }
        response_dict['selectedVerb'] = verb_dict
        correct_animation_dict = {
            'animationId': correct_animation.animationId,
            'imageAddress': correct_animation.imageAddress
        }
        response_dict['correctAnimation'] = correct_animation_dict
        invalid_animations_list = []
        for animation in invalid_animations:
            animation_dict = {
                'animationId': animation.animationId,
                'imageAddress': animation.imageAddress
            }
            invalid_animations_list.append(animation_dict)

        response_dict['invalidAnimations'] = invalid_animations_list

        return Response(response_dict)
