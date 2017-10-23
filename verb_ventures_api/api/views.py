from rest_framework import generics
from api.models import (
    VerbVentureUser,
    Admin,
    Student
)
from api.serializers import (
    VerbVentureUserSerializer,
    AdminSerializer,
    StudentSerializer
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
