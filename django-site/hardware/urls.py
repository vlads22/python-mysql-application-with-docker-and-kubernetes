from django.urls import path
from . import views

urlpatterns = [
    # map the index view from views to an url
    path("", views.index, name="index"),  # http://127.0.0.1:8000/polls/
]