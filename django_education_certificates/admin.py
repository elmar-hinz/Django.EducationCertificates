from django.contrib import admin
from django_education_certificates.models import Certificate, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Certificate)
