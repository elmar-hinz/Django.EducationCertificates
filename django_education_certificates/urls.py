from django.urls import path
from . import views

app_name="certificates"

urlpatterns = [
    # path('', views.CertificatesListView.as_view(), name='list'),
    path('', views.certificates, name='list'),
    path('<pk>', views.CertificatesDetailView.as_view(), name='detail'),
]