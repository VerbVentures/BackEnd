from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^users/$', views.VerbVentureUserList.as_view()),
    url(r'^admins/$', views.AdminListCreate.as_view()),
    url(r'^admins/(?P<pk>[0-9a-f-]+)$', views.AdminRetrieveUpdateDestroy.as_view()),
    url(r'^students/$', views.StudentListCreate.as_view()),
    url(r'^students/(?P<pk>[0-9a-f-]+)$', views.StudentRetrieveUpdateDestroy.as_view()),
]
