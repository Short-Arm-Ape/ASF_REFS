# middleware/token_refresh.py
from django.utils.deprecation import MiddlewareMixin
from msal import TokenCache

class AzureTokenRefreshMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            cache = TokenCache()
            cache.deserialize(request.user.access_token)
            
            app = get_msal_app()
            result = app.acquire_token_silent(
                settings.AZURE_AD["SCOPES"],
                account=request.user.azure_account,
                token_cache=cache
            )
            
            if result:
                request.user.access_token = cache.serialize()
                request.user.save()