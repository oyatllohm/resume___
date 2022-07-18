from django.contrib import admin
from django.urls import path ,include
from django.contrib.auth.urls import  urlpatterns
from django.conf import settings
from django.conf.urls.static import static
# from  django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT )
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )