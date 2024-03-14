from . import views
from django.urls import path

urlpatterns = [
    path("2nd/",views.second_app_function)
]