from . import views
from django.urls import path


urlpatterns = [
    path("1st/",views.machine),
    path("login/",views.login_user),
    path("reg/",views.register, name = "register"),
]