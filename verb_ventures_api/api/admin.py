from django.contrib import admin
from .models import (
    VerbVentureUser,
    Admin,
    Student,
    Session,
    Verb,
    Animation,
    VerbPack,
    LearnedVerb
)

admin.site.register(VerbVentureUser)
admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Session)
admin.site.register(Verb)
admin.site.register(Animation)
admin.site.register(LearnedVerb)
admin.site.register(VerbPack)
