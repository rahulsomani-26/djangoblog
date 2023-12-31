from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from djangoallfeaturesproject.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
