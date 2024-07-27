# myapp/blog/urls.py

from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("index.do", views.index.as_view(), name="main")
]
