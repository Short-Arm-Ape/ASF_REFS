# views.py
# 对应 Django 视图的权限检查（views.py）
@permission_required('app.call_api', raise_exception=True)
def api_view(request):
    # 调用 API 的逻辑
    pass

from msal import ConfidentialClientApplication

def get_msal_app():
    return ConfidentialClientApplication(
        client_id=settings.AZURE_AD["CLIENT_ID"],
        client_credential=settings.AZURE_AD["CLIENT_SECRET"],
        authority=settings.AZURE_AD["AUTHORITY"],
    )

from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
import requests

@login_required
@permission_required('app.call_api', raise_exception=True)
def api_view(request):
    # 获取访问令牌
    app = get_msal_app()
    result = app.acquire_token_silent(
        scopes=settings.AZURE_AD["SCOPES"],
        account=request.user.azure_account  # 假设已存储用户令牌信息
    )
    
    if not result:
        return JsonResponse({"error": "Unauthorized"}, status=401)

    # 调用受保护 API
    try:
        headers = {'Authorization': f'Bearer {result["access_token"]}'}
        response = requests.get(
            f"{settings.AZURE_AD['API_URI']}/your-api-path",
            headers=headers
        )
        response.raise_for_status()
        return JsonResponse(response.json())
    except requests.HTTPError as e:
        return JsonResponse({"error": str(e)}, status=500)
    
def handle_azure_error(e):
    error_data = {
        "error_type": "AzureADError",
        "code": e.error_code,
        "message": str(e),
        "timestamp": datetime.now().isoformat()
    }
    logger.error(json.dumps(error_data))
    return JsonResponse(error_data, status=500)