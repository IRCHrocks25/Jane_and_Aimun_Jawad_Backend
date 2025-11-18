"""
URL configuration for Centaura CMS project.
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def root_view(request):
    """Root endpoint that explains this is the API server"""
    return JsonResponse({
        'message': 'Centaura CMS API Server',
        'endpoints': {
            'api': '/api/',
            'dashboard': '/dashboard/',
            'admin': '/admin/',
        },
        'frontend': 'https://janeandaimunjawadfontend-production.up.railway.app'
    })

urlpatterns = [
    path('', root_view, name='root'),
    path('admin/', admin.site.urls),
    path('api/', include('content.urls')),
    path('dashboard/', include('dashboard.urls')),
]

