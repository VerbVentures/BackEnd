import uuid
from django.core.validators import RegexValidator
from django.db import models


class VerbVentureUser(models.Model):
    userId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.firstName, self.lastName)

class Admin(models.Model):
    accountKitId = models.CharField(primary_key=True, editable=True, max_length=16)
    user = models.ForeignKey(VerbVentureUser, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)

    def delete(self):
        self.user.delete()
        return self

    def __str__(self):
        return str(self.user)


class Student(models.Model):
    studentId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(VerbVentureUser, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

    def delete(self):
        self.user.delete()
        return self

    def __str__(self):
        return str(self.user)


class Session(models.Model):
    sessionId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sessionDt = models.DateField()
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    sessionStudents = models.ManyToManyField(Student)

    def __str__(self):
        return '%s (%s, %s)' % (str(self.session_id), str(self.admin), str(self.session_dt))


class Verb(models.Model):
    verbId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, blank=True, null=True)
    verb = models.CharField(max_length=20)
    definition = models.TextField()

    def __str__(self):
        return self.verb

class Animation(models.Model):
    animationId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    verb = models.ForeignKey(Verb, on_delete=models.CASCADE)
    imageAddress = models.URLField(max_length=2083)

    def __str__(self):
        return 'Animation for %s: %s' % (self.verb.verb, str(self.animationId))


class VerbPack(models.Model):
    verbPackId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=260)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    verbPackVerbs = models.ManyToManyField(Verb)
    userVerbPacks = models.ManyToManyField(VerbVentureUser)

    def __str__(self):
        return self.title


class LearnedVerb(models.Model):
    learnedVerbId =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    verb = models.ForeignKey(Verb, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, db_index=True, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, db_index=True, on_delete=models.CASCADE)
    animations = models.ManyToManyField(Animation)
    createdDt = models.DateTimeField(auto_now_add=True)
    correct = models.BooleanField()
    tries = models.IntegerField()

    def __str__(self):
        return str(self.learnedVerbId)
