# utils/decorators.py
from django.contrib.auth.decorators import user_passes_test

def api_call_permission_required(view_func):
    return user_passes_test(
        lambda u: u.has_perm('app.call_api') or u.is_superuser,
        login_url='/unauthorized/'
    )(view_func)