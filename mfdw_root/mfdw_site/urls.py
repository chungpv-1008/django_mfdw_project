from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quote/', include('quotes.urls')),
    path('', include('pages.urls')),
]
