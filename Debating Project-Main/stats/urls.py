from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login_view"),
    path("logout_view", views.logout_view, name="logout_view"),
    path("register", views.register, name="register"),
    path("speaks",views.getspeaks,name="getspeaks"),
    path("debaters",views.showdebaters,name="showdebaters"),
    path("institutions",views.show_ins,name="show_ins"),
    path("tournaments",views.showtourneys,name="showtourneys"),
]
