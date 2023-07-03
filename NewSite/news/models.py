from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to="photo/%Y/%m/%d", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['-time_create', 'title']

class Photo(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст', null=True)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo', kwargs={'photo_slug': self.slug})

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

class Message(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    email = models.EmailField(max_length=100, verbose_name='Почта')
    content = models.TextField(blank=True, verbose_name='Описание', )
    photo = models.ImageField(upload_to="photo/%Y/%m/%d", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщения'
        ordering = ['-time_create']

