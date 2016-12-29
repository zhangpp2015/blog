from django.conf.urls import include, url
from blog.views import *


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^archive$', archive, name='archive'),
    url(r'^tag$', tag, name='tag'),
    url(r'^category$', category, name='category'),
    url(r'^comment_post$', comment_post, name='comment_post'),
    url(r'^article$', article, name='article'),
    url(r'^login', do_login, name='login'),
    url(r'^logout', do_logout, name='logout'),
    url(r'^reg', do_reg, name='reg'),
    url(r'^about', about, name='about'),
]