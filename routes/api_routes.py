from flask import Blueprint, render_template
import requests
from services.auth_service import auth

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route("/call_api")
@auth.login_required(scopes=auth.app.config['SCOPE'])
def call_downstream_api(*, context):
    api_result = requests.get(
        auth.app.config['ENDPOINT'],
        headers={'Authorization': 'Bearer ' + context['access_token']},
        timeout=30,
    ).json() if context.get('access_token') else "Did you forget to set the SCOPE environment variable?"
    return render_template('display.html', title="API Response", result=api_result)
