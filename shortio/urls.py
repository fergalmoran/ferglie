from django.conf.urls import url, include
from django.contrib import admin

from dispatcher.views import dispatch
from shortio import settings
from shorts.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='home'),
    url(r'^shorts/', include('shorts.urls', namespace='urls')),
    url(r'^api/', include('shorts.urls', namespace='api')),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/', include('allauth.urls')),
    url(r'^(?P<dispatch_id>\w+)$', dispatch),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
