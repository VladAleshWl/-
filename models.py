# -*- coding: utf-8 -*-
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.utils import phone_format


class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):

        email = self.normalize_email(email)

        user = self.model(email=email, password=password, **kwargs)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)

        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('Электропочта'), max_length=255, unique=True)
    email_code = models.CharField(_('Код активации'), max_length=6, blank=True, null=True)
    name = models.EmailField(_('заглушка имени (требуется django)'), max_length=255, blank=True, null=True)
    date_joined = models.DateTimeField(_('Зарегистрирован'), auto_now_add=True)
    is_active = models.BooleanField(_('Активный'), default=True)
    is_staff = models.BooleanField(_('Модератор'), default=False)
    last_visited = models.DateTimeField(blank=True, null=True, verbose_name=_('Последнее посещение'))

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return u'{}'.format(self.email)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email
