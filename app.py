from flask import Flask  # 修正：添加 Flask 的导入
from config.settings import configure_app
from routes.auth_routes import auth_blueprint
from routes.api_routes import api_blueprint

app = Flask(__name__)
configure_app(app)  # 加载配置

# 注册蓝图
app.register_blueprint(auth_blueprint)
app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run(debug=True)  # 修正：添加 debug 参数以便开发调试

