
from django.contrib import admin
from django.urls import path
from autoc_part2.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home),
    path("name/",name,name="name"),
]
