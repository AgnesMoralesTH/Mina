from django.urls import path
from .views import RegisterPage,WordList, Newcomers, CustomLoginView,WordList
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name="register"),
    path('my-words/', WordList.as_view(),name='my-words'),
    path('',Newcomers.as_view(), name="newcomers")
]