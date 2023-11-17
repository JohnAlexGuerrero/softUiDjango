from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega datos adicionales al contexto si es necesario
        context['mi_dato'] = '¡Hola desde la vista basada en clases!'
        return context

class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "home/dashboard.html"
    login_url = '/accounts/sign-in/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega datos adicionales al contexto si es necesario
        context['mi_dato'] = '¡Hola desde la vista basada en clases!'
        return context