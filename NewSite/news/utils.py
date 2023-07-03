from .models import *

menu = [
    {'title': "Главная", 'url_name': 'home'},
    {'title': "Новости", 'url_name': 'news'},
    {'title': "Персонажи", 'url_name': 'gallery'},
    {'title': "Обучение", 'url_name': 'training'},
    {'title': "Помощь", 'url_name': 'help', },
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        news = News.objects.all()
        cats = Category.objects.all()
        photo = Photo.objects.all().order_by()
        context['menu'] = menu
        context['cats'] = cats
        context['news'] = news
        context['photo'] = photo
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context