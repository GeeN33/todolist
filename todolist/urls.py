

from django.contrib import admin
from django.urls import path, include

from bot.views import VerificationViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('goals/', include('goals.urls')),
    path('core/', include('core.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('api-auth/', include('rest_framework.urls')),
    path('bot/', include('bot.urls')),
]
