from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .views import Toll_Info,qr_generate,qr_read,profile

urlpatterns = [
    url(r'^toll_data/$',Toll_Info),
    url(r'^qr_generate/',qr_generate),
    url(r'^qr_read',qr_read),
    url(r'^profile',profile)
]
