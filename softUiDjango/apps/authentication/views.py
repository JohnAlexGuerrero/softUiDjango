from typing import Any
from django.db import models
from django.views.generic import TemplateView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from apps.authentication.forms import PerfileForm
from apps.authentication.forms import EmailForm

from apps.models import Profile

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/sign-up.html"

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = PerfileForm
    success_url = reverse_lazy('profile')
    template_name = "accounts/profile.html"
    
    def get_object(self):
        print(self.request.user.id)
        print(self.request.user)
        # try:
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
        # except Profile.DoesNotExist:
        #     return Profile.objects.create(user=self.request.user) 

@method_decorator(login_required, name='dispatch')  
class EmailUpdateView(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = "accounts/profile_email_form.html"

    def get_object(self):
        return self.request.user
