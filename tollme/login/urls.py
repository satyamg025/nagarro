from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .views import login,checking_otp,check_token

urlpatterns = [
    url(r'^user_login/$', login),
    url(r'^check_otp/$',checking_otp),
    url(r'^check_token/$',check_token),
    
]