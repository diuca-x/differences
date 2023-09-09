import os
from flask import jsonify, request, make_response

from flask_restful import Resource, abort
from flask_jwt_extended import create_access_token,jwt_required


#---import models
from models.users import User

#--- import db
from extensions import db


from flask import  render_template

from extensions import ph


class Signupator(Resource): #to get all questions, or create a new one
    method_decorators=[jwt_required()]
    def post(self):
        print("Asd")
        data = request.json
        user = data.get("user")
        password = data.get("password")
        rep_password = data.get("rep_password")
       
        if not user or not password:
            return make_response(jsonify({"msg" :  "missing data"}),400)
        if password != rep_password:
            return make_response(jsonify({"msg" : "passwords dont match"}),400)

        existe = User.query.filter_by(user=user).first()
    
        if existe: 
            return make_response(jsonify({"msg" : "User exists"}),400)

        hash = ph.hash(password)
        
        addUsuario = User(user = user, password=hash)
        print(addUsuario.serialize())
        db.session.add(addUsuario)
        db.session.commit()

        return jsonify({"msg" : "user registered"})
    

class Loginator(Resource): #to get all questions, or create a new one
    def post(self):
            data = request.json
            user = data.get("user")
            password = data.get("password")
            print(os.environ.get("JWT_SECRET_KEY"))
            
            if not user or not password:
                return make_response(jsonify({"msg" :  "missing data"}),400)
            
            hash = ph.hash(password)
            user = User.query.filter_by(user=user).first()

            if not user:
                return make_response(jsonify({"msg": "Wrong username or password"}), 400)
            else:
                try:
                    if(not ph.verify(user.password,password)):
                       
                        return make_response(jsonify({"msg": "Wrong username or password"}), 400)
                except: 
                    
                    return make_response(jsonify({"msg": "Wrong username or password"}), 400)
            
            token = create_access_token(identity=user.id)
            return jsonify({ "token": token, "msg":"login success"})
    
class Token_validator(Resource):
    method_decorators=[jwt_required()]
    def get(self):
        pass