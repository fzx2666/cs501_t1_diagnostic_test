from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

root_blueprint = Blueprint('rootpage', __name__)


class rootPage(MethodView):
    """
    User Display Resource
    """

    def get(self):

        return "Hey This is the Root Page. Please Browse into /index/users and /auth/register", 203


# define the API resources
root_view = rootPage.as_view('rootpage_api')

# add Rules for API Endpoints
root_blueprint.add_url_rule(
    '/',
    view_func=root_view,
    methods=['POST', 'GET']
)