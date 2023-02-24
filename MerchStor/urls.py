from django.conf.urls.static import static
from django.urls import path, include

from django.contrib import admin
from django.urls import path

from MerchStor import settings
from merch.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('merch/', include('merch.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound