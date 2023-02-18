
from django.contrib import admin
from django.urls import include, path
# For swagger documentation
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from rest_framework import permissions
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Smart Gantt Chart API",
        default_version='1.0.0',
        description="API documentation of Smart Gantt Chart Visualization",
     
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('smart-gantt-chart-admin/', admin.site.urls),
    path('triaging/', include('triaging.urls')),
    path('documentation', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api-token-auth/', views.obtain_auth_token),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
