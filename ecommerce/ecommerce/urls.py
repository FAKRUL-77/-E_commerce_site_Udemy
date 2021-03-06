from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('products.urls')),
  path('user/', include('customers.urls')),
  path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
