from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

display_blueprint = Blueprint('display', __name__)


class displayAPI(MethodView):
    """
    User Display Resource
    """

    def get(self):
        user = User.query.all()
        d = {}
        count = 0
        for column in user:
            d[count] = str(column.email)
            count = count+1
        #return make_response(d), 201
        return "please no error!", 201


# define the API resources
display_view = displayAPI.as_view('display_api')

# add Rules for API Endpoints
display_blueprint.add_url_rule(
    '/users/index',
    view_func=display_view,
    methods=['POST', 'GET']
)
