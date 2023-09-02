from extensions import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(), unique=False, nullable=False) 
    answer = db.Column(db.String(), unique=False, nullable=False)

    options = db.relationship("Options", backref="question", lazy = True)
    

    def serialize(self):
        serialized_options = [i.serialize()["option"] for i in self.options]
        return {
            "id": self.id,
            "question": self.question, 
            "answer": self.answer,
            "options" : serialized_options
        }
    
