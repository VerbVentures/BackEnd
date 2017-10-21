import uuid
from django.core.validators import RegexValidator
from django.db import models


class VerbVentureUser(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Admin(models.Model):
    admin_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(VerbVentureUser, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)


class Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(VerbVentureUser, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)


class Session(models.Model):
    session_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session_dt = models.DateField()
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    session_students = models.ManyToManyField(Student)


class Verb(models.Model):
    verb_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    verb = models.CharField(max_length=20)
    definition = models.TextField()


class Animation(models.Model):
    animation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    verb = models.ForeignKey(Verb, on_delete=models.CASCADE)
    image_address = models.URLField(max_length=2083)


class VerbPack(models.Model):
    verb_pack_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    verb_pack_verbs = models.ManyToManyField(Verb)
    user_verb_packs = models.ManyToManyField(VerbVentureUser)


class LearnedVerb(models.Model):
    learned_verb_id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    verb = models.ForeignKey(Verb, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    correct = models.BooleanField()
    tries = models.IntegerField()
