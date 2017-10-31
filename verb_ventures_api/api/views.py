from rest_framework import generics
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
    LearnedVerbSerializer
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
