from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<dispatch_id>\w+)/$', 'dispatcher.views.dispatch'),
]
