from django.urls import include, path
from api import views

urlpatterns = [
    path("ducksearch", views.search_view, name="duck-search"),
]
