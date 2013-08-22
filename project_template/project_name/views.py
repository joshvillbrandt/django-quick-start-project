from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
# For more information on this file, see
# https://docs.djangoproject.com/en/{{ docs_version }}/intro/tutorial03/

def home(request):
    template = loader.get_template('home.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))