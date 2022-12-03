# -*- coding: utf-8 -*-
import os

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image
from django.utils.translation import ugettext_lazy as _
from pytils.translit import slugify

from django.db.models.signals import pre_delete, post_save, pre_save
from django.dispatch import receiver

from core.models import TimeStampedModel, SeoModel


class News(TimeStampedModel, SeoModel, models.Model):

    IMAGE_SIZE_PC = (438, 438)
    IMAGE_SIZE_TEL = (350, 438)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='pages', verbose_name=_('Автор'), editable=True)
    name = models.CharField(verbose_name=_('Заголовок'), max_length=255)
    slug = models.SlugField(unique=False, editable=True, db_index=True)
    image = models.ImageField(verbose_name=_('Обложка'), null=True, blank=True)
    custom_code = models.TextField(verbose_name=_('Исполняемый код (html, css, js)'), null=True, blank=True)
    body = RichTextUploadingField(verbose_name=_('Содержание'), config_name='admin')  # models.TextField(verbose_name=_('Содержание'))

    is_draft = models.BooleanField(_('На модерации'), default=False)

    noindex = models.BooleanField(_('Скрыть от индексации поисковых ботов?'), default=False)

    def get_url(self):
        return reverse("news:item", kwargs={'slug': self.slug})

    def get_body(self):
        return self.body

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_image(self, mobile=False):

        if self.image:

            path = self.image.url + '.webp'

            if mobile:
                path = self.image.url + '.mobile.webp'

            return path

        return '/static/image/placeholder.webp'

    def generate_images(self):

        image = self.image

        if not image:
            return

        img_path = image.path

        if not os.path.isfile(img_path):
            return

        # create PC webp image

        image = Image.open(img_path)
        image = image.convert('RGB')
        image.thumbnail(self.IMAGE_SIZE_PC, Image.ANTIALIAS)
        image.save('{}.webp'.format(img_path), 'webp', optimize = True, quality = 100)
        image.close()

        # create MOBILE webp image

        image = Image.open(img_path)
        image = image.convert('RGB')
        image.thumbnail(self.IMAGE_SIZE_TEL, Image.ANTIALIAS)
        image.save('{}.mobile.webp'.format(img_path), 'webp', optimize = True, quality = 80)
        image.close()


    def delete_image(self):
        if self.image:

            webp_path = self.image.path + '.webp'
            webp_mobile_path = self.image.path + '.mobile.webp'

            if os.path.isfile(webp_path):
                os.remove(webp_path)

            if os.path.isfile(webp_mobile_path):
                os.remove(webp_mobile_path)

            if os.path.isfile(self.image.path):
                os.remove(self.image.path)

    class Meta:

        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')



@receiver(pre_delete, sender=News)
def news_pre_delete(instance, **kwargs):

    instance.delete_image()



@receiver(pre_save, sender=News)
def news_pre_create(instance, **kwargs):

    real_instance = News.objects.filter(pk=instance.id).first()
    if real_instance:
        real_instance.delete_image()


@receiver(post_save, sender=News)
def news_post_create(instance, **kwargs):

    instance.generate_images()

