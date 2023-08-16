from django.urls import path

# We want a path that is attatched to our views py file
from . import views

# Path spec, where this is in our views, the name we are giving it
urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
]
