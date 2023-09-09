from flask import Blueprint, render_template
from api.admin_routes import Loginator, Signupator,Token_validator
from flask_restful import Api

from api.resources.routes import Compareimg

blueprint = Blueprint("api", __name__, url_prefix="/api")
auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

api = Api(blueprint, errors=blueprint.errorhandler)
auth =  Api(auth_blueprint, errors=auth_blueprint.errorhandler)


api.add_resource(Compareimg, "/compare")


auth.add_resource(Signupator, "/signupator")
auth.add_resource(Loginator, "/loginator")
auth.add_resource(Token_validator, "/validator")

@auth_blueprint.route("/login")
def login(): 
   return render_template("login.html")

@auth_blueprint.route("/home")
def home(): 
   return render_template("home.html")


@auth_blueprint.route("/signup")
def signup(): 
     return render_template("signup.html")

@auth_blueprint.route("/img")
def img_loader():
    return render_template("img_loader.html")