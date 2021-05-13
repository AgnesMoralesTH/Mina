from django.urls import path
from .views import RegisterPage, WordDetail,WordList, Newcomers, CustomLoginView,WordList, WordCreate, WordUpdate
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('word-create/', WordCreate.as_view(), name='word-create'),
    path('word-update/<int:pk>', WordUpdate.as_view(), name="word-update"),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name="register"),
    path('my-words/', WordList.as_view(),name='my-words'),
    path('',Newcomers.as_view(), name="newcomers"),
    path('word/<int:pk>/', WordDetail.as_view(), name="word")
]