# -*- coding:utf-8 -*-

from django.views.generic import CreateView, RedirectView, FormView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import logout
from django.http import JsonResponse

from .forms import AuthForm
from core.mixins import GuestMixin, UserMixin
from core.views import RequestFormView


class LogoutView(RedirectView):
    permanent = False
    query_string = True
    url = reverse_lazy('user:auth')

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class CreateOrLoginView(GuestMixin, RequestFormView, FormView):

    form_class = AuthForm
    template_name = 'user/auth.jinja'
    success_url = reverse_lazy('user:private')

    def form_valid(self, form):
        response = super(CreateOrLoginView, self).form_valid(form)
        if self.request.is_ajax():
            return JsonResponse({'success': 1}, safe=False)
        return response

    def form_invalid(self, form):
        response = super(CreateOrLoginView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse({'errors': form.errors.as_json()}, safe=False)
        return response


class PrivateView(UserMixin, TemplateView):

    template_name = 'user/private.jinja'

    def get_context_data(self, **kwargs):

        context = super(PrivateView, self).get_context_data(**kwargs)

        return context
