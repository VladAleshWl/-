from django.conf.urls import url
from .views import (
    LogoutView, CreateOrLoginView,
    PrivateView, 
)

urlpatterns = [
    url(r'^auth/$', CreateOrLoginView.as_view(), name='auth'),
    url(r'^private/$', PrivateView.as_view(), name='private'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
