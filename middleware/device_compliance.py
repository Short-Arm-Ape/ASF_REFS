# middleware/device_compliance.py
from django.http import JsonResponse

class DeviceComplianceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/'):  # 只拦截 API 请求
            if not check_device_compliance(request):
                return JsonResponse(
                    {"error": "Device not compliant"},
                    status=403
                )
        return self.get_response(request)