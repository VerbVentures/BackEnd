from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^users/$', views.VerbVentureUserList.as_view()),
    url(r'^admins/$', views.AdminListCreate.as_view()),
    url(r'^admins/(?P<pk>[0-9a-f-]+)/$', views.AdminRetrieveUpdateDestroy.as_view()),
    url(r'^students/$', views.StudentListCreate.as_view()),
    url(r'^get-admin-students/(?P<pk>[0-9a-f-]+)/$', views.StudentList.as_view()),
    url(r'^get-admin-verbs/(?P<pk>[0-9a-f-]+)/$', views.VerbList.as_view()),
    url(r'^get-user-verbpacks/(?P<pk>[0-9a-f-]+)/$', views.VerbPackList.as_view()),
    url(r'^students/(?P<pk>[0-9a-f-]+)/$', views.StudentRetrieveUpdateDestroy.as_view()),
    url(r'^sessions/$', views.SessionListCreate.as_view()),
    url(r'^sessions/(?P<pk>[0-9a-f-]+)/$', views.SessionRetrieveUpdateDestroy.as_view()),
    url(r'^verbs/$', views.VerbListCreate.as_view()),
    url(r'^verbs/(?P<pk>[0-9a-f-]+)/$', views.VerbRetrieveUpdateDestroy.as_view()),
    url(r'^animations/$', views.AnimationListCreate.as_view()),
    url(r'^animations/(?P<pk>[0-9a-f-]+)/$', views.AnimationRetrieveUpdateDestroy.as_view()),
    url(r'^verbpacks/$', views.VerbPackListCreate.as_view()),
    url(r'^verbpacks/(?P<pk>[0-9a-f-]+)/$', views.VerbPackRetrieveUpdateDestroy.as_view()),
    url(r'^learnedverb/$', views.LearnedVerbListCreate.as_view()),
    url(r'^learnedverb/(?P<pk>[0-9a-f-]+)/$', views.LearnedVerbRetrieveUpdateDestroy.as_view()),
]
