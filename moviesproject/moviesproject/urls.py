from django.contrib import admin
from django.urls import path
from moviesapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]