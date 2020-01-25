from django.urls import path
from . import views


urlpatterns = [
    path("",views.gbook,name='index'),
    path("sign/",views.sign,name='sign')
]
