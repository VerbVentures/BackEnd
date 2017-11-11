from rest_framework import generics
from django.db.models import Q
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
