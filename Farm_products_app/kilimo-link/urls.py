from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

api_urls = [
    path('products/', include('products.urls')),
    path('', include('users.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
