from django.conf.urls import include, url

from shorts import views
from .api import UrlList, UrlDetail, UserUrlList
# from .api import UserList, UserDetail

user_urls = [
    url(r'^(?P<username>[0-9a-zA-Z_-]+)/urlss$', UserUrlList.as_view(), name='userurl-list'),
    # url(r'^(?P<username>[0-9a-zA-Z_-]+)$', UserDetail.as_view(), name='user-detail'),
    # url(r'^$', UserList.as_view(), name='user-list')
]

urls_urls = [
    url(r'^(?P<pk>\d+)$', UrlDetail.as_view(), name='urls-detail'),
    url(r'^$', UrlList.as_view(), name='urls-list')
]

urlpatterns = [
    url(r'^users', include(user_urls)),
    url(r'^urls', include(urls_urls)),
    url(r'^$', views.index, name='index'),
    url(r'^create', views.create, name='create'),
    url(r'^(?P<url_id>\d+)/$', views.detail, name='detail')
]
