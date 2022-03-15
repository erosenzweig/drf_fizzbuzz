from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # REST FRAMEWORK URLS
    path('api/', include('api.urls', 'api'))
]
