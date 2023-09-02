from flask import Blueprint
from flask_restful import Api

from api.resources.routes import SingleQuestion, specificQuestion, addOptions, handleOption

blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(blueprint, errors=blueprint.errorhandler)

api.add_resource(SingleQuestion, "/question")
api.add_resource(specificQuestion, "/question/<int:question_id>")
api.add_resource(addOptions, "/addOptions/<int:question_id>")
api.add_resource(handleOption, "/handleOption/<int:option_id>")