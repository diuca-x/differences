from extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(), nullable=False) 
    password = db.Column(db.String(), unique=False, nullable=False)
    
    #cliente = db.relationship("Cliente", backref="usuario", lazy = True)
    

    def serialize(self):
        
        return {
            "id": self.id,
            "user": self.user, 
            "password": self.password,  
        }