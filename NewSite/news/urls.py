
from django.urls import include, path
from news.views import *

urlpatterns = [
    path('', index, name="home"),
    path('news/', NewsHome.as_view(), name="news"),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('help/', Help.as_view(), name="help"),
    path('gal/', GalleryHome.as_view(), name="gallery"),
    path('photo/<slug:photo_slug>/', ShowPhoto.as_view(), name='photo'),
    path('category/<slug:cat_slug>/', PhotoCategory.as_view(), name='category'),
    path('training/', training, name="training"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
    path('register', RegisterUser.as_view(), name='register'),
]

