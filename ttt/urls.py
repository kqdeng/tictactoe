from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('play', views.play, name="play"),
    # path('adduser', views.add_user, name="adduser")
]
