from App import db

class User(db.Model):
    id = db.Coloumn(db.Integer, primary_key=True)
    username= db.Coloumn(db.String(64), index=True, unique=True)
    email= db.Coloumn(db.String(120), index=True, unique=True)
    password_hash= db.Coloumn(db.String(128))

    def __repr__(self):
        return '<User{}>'.format(self.username)