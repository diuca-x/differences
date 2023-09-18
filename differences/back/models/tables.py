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
        
        coors1 =  tuple(map(int, self.cor1.split(',')))
        coors2 =  tuple(map(int, self.cor2.split(',')))
        coors3 =  tuple(map(int, self.cor3.split(',')))
        coors4 =  tuple(map(int, self.cor4.split(',')))
        coors5 =  tuple(map(int, self.cor5.split(',')))
        coors6 =  tuple(map(int, self.cor6.split(',')))
        coors7 =  tuple(map(int, self.cor7.split(',')))
        coors8 =  tuple(map(int, self.cor8.split(',')))
            
        return {
            "id": self.id,
            "og_url": self.og_url, 
            "diff_url": self.diff_url,
            "coors" :[ coors1,coors2,coors3,coors4,coors5,coors6,coors7,coors8],
            "date" : self.date.strftime("%d/%m/%Y")
        }
    
