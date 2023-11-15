from django.urls import path

from apps.authentication.views import RegisterView, LoginView

urlpatterns = [
    path('sign-in/', LoginView.as_view(), name='sign-in'),
    path('sign-up/', RegisterView.as_view(), name='sign-up'),
]
