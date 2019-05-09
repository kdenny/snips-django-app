from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from . import views

urlpatterns = [
    url(r'^yaml/$', views.MakeYAMLFromDB.as_view()),
    url(r'^json/$', views.MakeJSONFromDB.as_view()),
    url(r'^parse/$', views.CommandsParse.as_view()),
    url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True)))
]