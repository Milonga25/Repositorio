from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.models import Group, User

# Create your views here.

class RegistrarUsuario(CreateView):
    model = User
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioForm

    def get_success_url(self):
        next_url = self.request.POST.get('next') or self.request.GET.get('next')
        if next_url and next_url != 'None':
            return next_url
        return reverse_lazy('apps.usuario:login') 

class LoginUsuario(LoginView):
    def get_success_url(self):
        next_url = self.request.POST.get('next') or self.request.GET.get('next')
        if next_url and next_url != 'None':
            return next_url
        return reverse_lazy('apps.posts:posts') 

class LogoutUsuario(LogoutView):

    def get_success_url(self):
        messages.success(self.request, 'Logout exitoso')
        return reverse('index')
