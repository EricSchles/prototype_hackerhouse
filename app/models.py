from app import app,db

#http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(300),unique=True)
    password = db.Column(db.String(400))
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def __repr__(self):
        return self.username


