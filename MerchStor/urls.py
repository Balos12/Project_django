from django.urls import path, include

from django.contrib import admin
from django.urls import path

from merch.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('merch/', include('merch.urls')),
]
