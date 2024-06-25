from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'), #by setting first path to "", it will be the default page istead oh 'home
    # path('authorised', views.AuthorisedView.as_view(), name='authorised'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
]