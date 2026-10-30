from django.contrib import admin
from django.urls import path
from moviesapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('users/', create_user, name="create_user"),
    path('users/login/', login_user, name="login"),
    path('users/logout/', logout_user, name="logout"),
]
