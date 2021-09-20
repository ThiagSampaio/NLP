#from app import db

class Feedback(db.Model):
    __tablename__ = 'termo'
    id = db.Column(db.Integer, primary_key=True)
    termo = db.Column(db.String(200))

    def __init__(self, termo):
        self.termo = termo