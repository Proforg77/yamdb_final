from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        'redoc/',
        TemplateView.as_view(template_name='api/redoc.html'),
        name='redoc'
    ),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
