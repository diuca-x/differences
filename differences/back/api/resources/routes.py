from flask import jsonify, request, make_response
from flask_restful import Resource, abort

#---import models
from models.tables import Images

#--- import db
from extensions import db


    
#class specificQuestion(Resource): 
    
    #def delete(self, question_id): 
       #pass

    
#class handleOption(Resource): 
    
    
    #def put(self,option_id):
        #data = request.json
        #pass
    
class asd(Resource):

    def get(self):
        a = Images.query.get(1)
        print(a.serialize())