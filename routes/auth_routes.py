from flask import Blueprint, render_template
from services.auth_service import auth

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route("/")
@auth.login_required
def index(*, context):
    return render_template(
        'index.html',
        user=context['user'],
        edit_profile_url=auth.get_edit_profile_url(),
        api_endpoint=auth.app.config['ENDPOINT'],
        title="Flask Web App Sample",
    )
