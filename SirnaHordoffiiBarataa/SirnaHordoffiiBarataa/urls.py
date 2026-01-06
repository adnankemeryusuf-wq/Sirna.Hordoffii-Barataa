from django.contrib import admin
from django.urls import path, include # 'include' asitti daballee jirra

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hordoffii.urls')), # Karaa appii hordoffii saaqneerra
]