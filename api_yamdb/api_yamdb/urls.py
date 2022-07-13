from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'
handler403 = 'core.views.csrf_failure'

urlpatterns = [
    path(
        'redoc/',
        TemplateView.as_view(template_name='api/redoc.html'),
        name='redoc'
    ),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
