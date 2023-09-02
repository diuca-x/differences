from extensions import db


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    og_url = db.Column(db.String(), unique=False, nullable=False) 
    diff_url = db.Column(db.String(), unique=False, nullable=False)
    marked_url = db.Column(db.String(), unique=False, nullable=False)

    #options = db.relationship("Options", backref="question", lazy = True)
    

    def serialize(self):
        
        return {
            "id": self.id,
            "og_url": self.og_url, 
            "diff_url": self.diff_url,
            "marked_url" : self.marked_url
        }
    
