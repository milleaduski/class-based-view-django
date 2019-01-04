from django.contrib import admin
from django.urls import path, include

from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tutorial/', IndexView.as_view()),
	path('accounts/', include('django.contrib.auth.urls'))
]