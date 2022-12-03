# -*- coding:utf-8 -*-

from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth import authenticate, login

from core.forms import RequestForm
from .models import User


class AuthForm(RequestForm, forms.Form):


    email = forms.CharField(label=_('EMAIL'), widget=forms.TextInput(attrs={'type': 'email', 'placeholder': _('EMAIL')}), required=True)
    password = forms.CharField(label=_('ПАРОЛЬ'), widget=forms.PasswordInput(attrs={'placeholder': _('ПАРОЛЬ')}))

    def clean_password(self):

        password = self.cleaned_data.get('password')

        return password

    def clean_email(self):

        email = self.cleaned_data.get('email')

        try:
            user = User.objects.get(email=email)
            if not user.is_active:
                raise forms.ValidationError(_('Учётная запись заблокирована.'))
        except:
            pass
        #     raise forms.ValidationError(_('Пользователь не найден.'))

        return email

    def clean(self):

        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        is_email_exists = User.objects.filter(email=email)

        if is_email_exists:

            user = authenticate(
                username=email,
                password=password
            )

            if user is None:
                raise forms.ValidationError(_('Неверный пароль или электропочта.'))

            login(self.request, user)

        else:

            user = User.objects.create_user(
                name='Пользователь{}'.format(User.objects.count()),
                email=email,
                password=password,
            )

            user = authenticate(
                username=email,
                password=password
            )

            login(self.request, user)

            if self.request.is_ajax():
                return {'success': 1}
            else:
                return user

