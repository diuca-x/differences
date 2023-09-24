from datetime import datetime
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
        return jsonify(a.serialize())
    
class start_game(Resource):
    def get(self):
        today_images = Images.query.filter_by(date = datetime.today().replace(hour=0, minute=0, second=0,microsecond=0 )).first()
        if today_images == None:
            today_images =Images.query.first()
        serialized_images = today_images.make_game_img()
        
        

        return jsonify(serialized_images)




