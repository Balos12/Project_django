from django.urls import path, include

from django.contrib import admin
from django.urls import path

from merch.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('merch/', include('merch.urls')),
]

handler404 = pageNotFound