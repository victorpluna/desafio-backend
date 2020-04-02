from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import permissions
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='Tembici API',
        default_version='v1',
        description='API para dar review nas viagens',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_v1_urls = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('trips/', include('trips.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_v1_urls)),
]

if settings.DEBUG:
    urlpatterns += [
        path(
            'swagger/',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'
        ),
        path(
            'redoc/',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'
        ),
    ]
