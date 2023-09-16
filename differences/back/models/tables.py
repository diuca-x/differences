from sqlalchemy import ARRAY, Integer
from extensions import db


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    og_url = db.Column(db.String(), unique=False, nullable=False) 
    diff_url = db.Column(db.String(), unique=False, nullable=False)
    cor1 = db.Column(db.String(), unique=False, nullable=False)
    cor2 = db.Column(db.String(), unique=False, nullable=False)
    cor3 = db.Column(db.String(), unique=False, nullable=False)
    cor4 = db.Column(db.String(), unique=False, nullable=False)
    cor5 = db.Column(db.String(), unique=False, nullable=False)
    cor6 = db.Column(db.String(), unique=False, nullable=False)
    cor7 = db.Column(db.String(), unique=False, nullable=False)
    cor8 = db.Column(db.String(), unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=False)

    #options = db.relationship("Options", backref="question", lazy = True)
    

    def serialize(self):
        
        return {
            "id": self.id,
            "og_url": self.og_url, 
            "diff_url": self.diff_url,
            "cors" :[ self.cor1,self.cor2,self.cor3,self.cor4,self.cor5,self.cor6,self.cor7,self.cor8],
            "date" : self.date.strftime("%d/%m/%Y")
        }
    
