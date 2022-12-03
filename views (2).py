from django.http import JsonResponse, Http404
from django.views.generic import View, TemplateView, DetailView, ListView, FormView
from django.shortcuts import render_to_response
from django.template import RequestContext

from news.models import News


class RequestFormView(View):

    def get_form_kwargs(self):

        kwargs = super(RequestFormView, self).get_form_kwargs()
        kwargs['request'] = self.request

        return kwargs


class Home(TemplateView):

    template_name = 'index.jinja'

    def get_context_data(self, **kwargs):

        context = super(Home, self).get_context_data(**kwargs)

        context['items'] = News.objects.all().order_by('-created_at')

        context['title'] = 'test'

        return context


def handler404(request):

    response = render_to_response('404.html', {}, RequestContext(request))
    response.status_code = 404

    return response


def handler500(request):

    response = render_to_response('500.html', {}, RequestContext(request))
    response.status_code = 500

    return response
