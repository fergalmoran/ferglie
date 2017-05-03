from django.shortcuts import render_to_response
from django.template import RequestContext


def get_template(request, template_name):
    return render_to_response(
        'dialogs/%s.html' % template_name,
        context_instance=RequestContext(request))
