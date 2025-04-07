import os

def configure_app(app):
    app.config['AUTHORITY'] = os.getenv("AUTHORITY")
    app.config['CLIENT_ID'] = os.getenv("CLIENT_ID")
    app.config['CLIENT_SECRET'] = os.getenv("CLIENT_SECRET")
    app.config['REDIRECT_URI'] = os.getenv("REDIRECT_URI")
    app.config['OIDC_AUTHORITY'] = os.getenv("OIDC_AUTHORITY")
    app.config['B2C_TENANT_NAME'] = os.getenv('B2C_TENANT_NAME')
    app.config['SIGNUPSIGNIN_USER_FLOW'] = os.getenv('SIGNUPSIGNIN_USER_FLOW')
    app.config['EDITPROFILE_USER_FLOW'] = os.getenv('EDITPROFILE_USER_FLOW')
    app.config['RESETPASSWORD_USER_FLOW'] = os.getenv('RESETPASSWORD_USER_FLOW')
    app.config['ENDPOINT'] = os.getenv("ENDPOINT")
    app.config['SCOPE'] = os.getenv("SCOPE", "").split()
