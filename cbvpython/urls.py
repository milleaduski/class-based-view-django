from django.contrib import admin
from django.urls import path

from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tutorial/', IndexView.as_view())
]