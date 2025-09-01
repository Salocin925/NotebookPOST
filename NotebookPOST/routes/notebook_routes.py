from flask import Blueprint, request
from controllers.notebook_controllers import create_notebook

notebook_routes = Blueprint('notebook_routes', __name__)

@notebook_routes.route('/Notebook', methods=['POST'])
def notebook_post():
    notebook_data = request.json
    return create_notebook(request.json)