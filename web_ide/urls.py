from django.contrib import admin
from django.urls import path

from ide.views import WebIDEView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WebIDEView.as_view(), name='ide'),
]
