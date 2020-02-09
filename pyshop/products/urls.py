from django.urls import path,include
from . import views

app_name="products"
urlpatterns = [
    path("",views.index,name="index"),
    path("news/<int:num>",views.test1,name="news"),
    path("newman/",views.forms,name="newman"),
    path("get/",views.get)
]
