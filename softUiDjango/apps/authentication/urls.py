from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.authentication.views import ProfileUpdate, SignUp, EmailUpdateView

urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('profile/email/', EmailUpdateView.as_view(), name='profile-email'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
