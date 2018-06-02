from app import db


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    counter_unique_words = db.Column(db.Integer)

    def __repr__(self):
        return '<Note №{}>'.format(self.id)