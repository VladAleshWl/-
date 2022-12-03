from django.http import HttpResponseRedirect
from django.views.generic import View


class GuestMixin(View):

    def dispatch(self, request, *args, **kwargs):

        if request.user.id:
            return HttpResponseRedirect('/')

        return super(GuestMixin, self).dispatch(request, *args, **kwargs)


class UserMixin(View):

    def dispatch(self, request, *args, **kwargs):

        if not request.user.id:
            return HttpResponseRedirect('/')

        return super(UserMixin, self).dispatch(request, *args, **kwargs)
