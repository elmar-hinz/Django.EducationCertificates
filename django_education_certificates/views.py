from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView
from . import models
from .models import Category
from .models import Certificate
from types import SimpleNamespace

# Create your views here.
class CertificatesListViewOld(ListView):
    context_object_name = 'certificates'
    model = Certificate

def certificates(request):
    categories = []
    for category in Category.objects.all():
        c = SimpleNamespace()
        c.name = category.name
        c.description = category.description
        c.certificates = category.certificate_set.all()
        categories.append(c)
    context = {"categories": categories}
    template = loader.get_template(
        'django_education_certificates/certificate_list.html')
    return HttpResponse(template.render(context, request))

class CertificatesDetailView(DetailView):
    context_object_name = 'certificate'
    model = Certificate



