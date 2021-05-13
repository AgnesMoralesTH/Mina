from django.contrib.auth.views import LoginView
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Word
from django.views.generic import TemplateView
from django.views import View 

from django.urls import reverse_lazy
# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields='__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('my-words')

class Newcomers(TemplateView):
    template_name = "base/PageForNewcomers.html"




class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('my-words')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('my-words')
        return super(RegisterPage, self).get(*args, **kwargs)



class WordDetail(LoginRequiredMixin, DetailView):
    model = Word
    context_object_name = 'task'
    template_name = 'base/task.html'

class WordList(LoginRequiredMixin,ListView):
    model = Word
    context_object_name = 'mywords'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mywords'] = context['mywords'].filter(user=self.request.user)
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['my-words'] = context['my-words'].filter(title__startswith=search_input)

        context['search_input'] = search_input   
        return context
    

    

class WordCreate(LoginRequiredMixin, CreateView):
        model = Word
        fields = ['title', 'description']
        success_url = reverse_lazy('my-words')

        def form_valid(self, form):
            form.instance.user = self.request.user
            return super(WordCreate, self).form_valid(form)


class WordUpdate(LoginRequiredMixin, DetailView):
    model = Word
    fields = ['title', 'description']
    success_url = reverse_lazy('my-words')


    
