# -*- coding:utf-8 -*-

from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, Http404
from django.conf import settings

from .models import News


class NewsItem(DetailView):

    model = News
    template_name = 'news/item.jinja'
    slug_url_kwarg = 'slug'
    context_object_name = 'item'

    def get_page_title(self):

        if self.object.seo_title:
            return self.object.seo_title

        return self.object.name

    def get_context_data(self, **kwargs):

        context = super(NewsItem, self).get_context_data(**kwargs)
        context['title'] = self.get_page_title()

        return context
