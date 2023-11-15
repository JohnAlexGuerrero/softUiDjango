from django.views.generic import TemplateView

class LoginView(TemplateView):
    template_name = "accounts/sign-in.html"


class RegisterView(TemplateView):
    template_name = "accounts/sign-up.html"
