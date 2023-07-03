from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *
from .utils import *

class NewsHome(DataMixin, ListView):
    paginate_by = 3
    model = News
    template_name = 'news/SMI.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class GalleryHome(DataMixin, ListView):
    model = Photo
    template_name = 'news/gallery.html'
    context_object_name = 'photo'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Photo.objects.filter(is_published=True)


class PhotoCategory(ListView):
    model = Photo
    template_name = 'news/gallery.html'
    context_object_name = 'photo'
    allow_empty = False

    def get_queryset(self, *, object_list=None, **kwargs):
        return Photo.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['photo'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['photo'][0].cat_id
        return context

class Help(DataMixin, CreateView):
    form_class = MessageForm
    template_name = 'news/help.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Помощь')
        return dict(list(context.items()) + list(c_def.items()))


def index(request):
    return render(request, 'news/index.html', {'menu': menu, 'title': 'Главная страница'})


def training(request):
    return render(request, 'news/training.html', {'menu': menu, 'title': 'Обучение'})



class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'news/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'news/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('home')


class ShowPost(DataMixin, DetailView):
    model = News
    template_name = 'news/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

class ShowPhoto(DetailView):
    model = Photo
    template_name = 'news/photo.html'
    context_object_name = 'photo'
    slug_url_kwarg = 'photo_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['photo']
        context['menu'] = menu
        return context




def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')
