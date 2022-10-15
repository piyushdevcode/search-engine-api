from django.urls import include, path
from api import views

urlpatterns = [
    path("", views.home, name="home"),
]
