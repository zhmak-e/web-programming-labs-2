from . import db
from flask_login import UserMixin

class users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(30), nullable=False, unique=True)
    password=db.Column(db.String(102), nullable=False)


    def __repr__(self):
        return f'id:{self.id}, username:{self.username}'
    
class articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    title=db.Column(db.String(50), nullable=False)
    article_text=db.Column(db.Text, nullable=False)
    is_favourite=db.Column(db.Boolean)
    is_public=db.Column(db.Boolean)
    likes=db.Column(db.Integer)

    def __repr__(self):
        return f'title:{self.title}, article_text:{self.article_text}'