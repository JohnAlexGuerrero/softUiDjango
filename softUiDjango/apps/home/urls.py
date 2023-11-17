from django.urls import path

from apps.home.views import Home, Dashboard

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='home_dashboard'),
]
