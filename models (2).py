# coding=utf-8
from django.db import models
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from PIL import Image
import os


# GEO
from django.contrib.gis.db import models as geo_models


class CoreConfig(AppConfig):
    name = 'core'
    verbose_name = _(u"Основное")


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Последнее обновление'))

    class Meta:
        abstract = True


class SeoModel(models.Model):
    seo_title = models.CharField(verbose_name=_('SEO-заголовок'), max_length=255, null=True, blank=True)
    seo_description = models.TextField(verbose_name=_('SEO-описание'), null=True, blank=True)
    # seo_tags

    class Meta:
        abstract = True
