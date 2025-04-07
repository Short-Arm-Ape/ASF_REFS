# 对应 Django 视图的权限检查（views.py）
@permission_required('app.call_api', raise_exception=True)
def api_view(request):
    # 调用 API 的逻辑
    pass