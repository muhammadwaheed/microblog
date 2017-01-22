from app import db


class Users(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(100), index=True, unique=True)

    def __repr__(self):

        return '<Users %r>' % (self.nickname)

