# urls.py
urlpatterns = [
    path("identity/", include("identity.urls", namespace="identity")),
]
