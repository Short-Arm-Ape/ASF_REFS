# urls.py
urlpatterns = [
    path("identity/", include("identity.urls", namespace="identity")),
]

from .views import api_view

urlpatterns = [
    path('api/', api_view, name='api_view'),
    path('api/healthcheck', healthcheck_view, name='api_healthcheck'),
]