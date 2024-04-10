from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.views.generic import FormView
from .models import Message
from .forms import MessageForm

# Create your views here.

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/'
    

class LoginView(LoginView):
    success_message = 'Hello %(username)s!'
    redirect_authenticated_user = True
    

class UserList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'users'

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        print(self.request.user)
        print(self.request.user.id)
        return qs.exclude(id=self.request.user.id)


class MessageDetailView(LoginRequiredMixin, ListView, FormView):
    model = Message
    context_object_name = 'messages'
    form_class = MessageForm
    success_url = '#'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        other_user = User.objects.get(pk=self.kwargs.get('pk'))
        messages = Message.objects.filter(
            sender=self.request.user,
            receiver=other_user
        ) | Message.objects.filter(
            sender=other_user,
            receiver=self.request.user
        ).order_by('created_at')

        context = super().get_context_data(**kwargs)
        context['other_user'] = other_user
        context['messages'] = messages
        return context

    def form_valid(self, form):
        form.instance.sender = self.request.user
        form.instance.receiver = User.objects.get(pk=self.kwargs.get('pk'))
        form.save()
        return super().form_valid(form)
    


class IndexView(TemplateView):
    template_name = 'index.html'