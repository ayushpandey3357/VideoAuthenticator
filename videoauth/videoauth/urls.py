import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from video import views as video_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('video/', include('video.urls')),
    path('', RedirectView.as_view(url='/video/')),
    path('account/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('account/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('account/register/', video_views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static')) if hasattr(settings, 'STATIC_ROOT') and settings.STATIC_ROOT else []
