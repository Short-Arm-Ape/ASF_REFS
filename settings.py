# 身份验证配置
AZURE_AD = {
    "TENANT_ID": "your_tenant_id",
    "CLIENT_ID": "your_client_id",  # 前端应用的客户端ID
    "CLIENT_SECRET": "your_client_secret",
    "AUTHORITY": "https://login.microsoftonline.com/your_tenant_id",
    "SCOPES": ["api://a09cdb24-5c48-475e-bb97-42d626ea2dea/CallAPI.All"],  # 对应 Entra ID 配置的作用域
    "API_URI": "https://your-api-endpoint.com",  # 实际 API 地址
    "REDIRECT_PATH": "/identity/redirect",  # 与 Entra ID 注册的回调地址一致
}

MIDDLEWARE = [
    ...
    'yourapp.middleware.device_compliance.DeviceComplianceMiddleware',
]