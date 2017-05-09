# Create your views here.
from django.http.response import Http404, HttpResponseRedirect

from core import url
from shorts.models import Url


def dispatch(request, dispatch_id):
    try:
        u = Url.objects.get(shortened_url=dispatch_id)
        return HttpResponseRedirect(u.url)
    except Url.DoesNotExist:
        raise Http404()
