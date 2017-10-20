from __future__ import absolute_import
from django.views import generic

from braces import views

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy

from .forms import RegistrationForm
from .forms import LoginForm


class HomePageView(generic.TemplateView):
    template_name = 'home.html'


class SignUpView(generic.CreateView, views.AnonymousRequiredMixin, views.FormValidMessageMixin):
    form_valid_message = "Inregistrare reusita!"
    form_class = RegistrationForm
    model = User
    template_name = 'accounts/signup.html'


class LoginView(generic.FormView, views.LoginRequiredMixin):
    form_class = LoginForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogOutView(generic.RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)






